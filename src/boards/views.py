from django.utils import timezone
from django.db.models import Count
from django.urls import resolve,reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView,ListView

from .forms import NewTopicForm,PostForm, NewBoardForm
from .models import Board,Topic,Post

class BoardListView(ListView):

	model = Board
	context_object_name = 'boards'
	template_name = 'boards/index.html'

class BoardTopicsListView(ListView):

	model = Topic
	context_object_name = 'topics'
	template_name = 'boards/topics.html'
	paginate_by = 5


	def get_context_data(self,**kwargs):
		"""
		overrides context
		"""
		kwargs['board'] = self.board
		return super().get_context_data(**kwargs)


	def get_queryset(self):
		"""
		overrides queryset
		"""
		self.board = get_object_or_404(Board,pk=self.kwargs.get('pk'))
		queryset = self.board.topics.annotate(replies = Count('posts') - 1)
		return queryset

@login_required
def new_topic(request,pk):

	current_user = request.user

	context = dict()
	board = get_object_or_404(Board,id = pk)
	form =  NewTopicForm()
	if request.method == 'POST':
		form =  NewTopicForm(data = request.POST)
		if form.is_valid():
			topic_instance = form.save(commit=False)
			topic_instance.board = board
			topic_instance.starter = current_user
			topic_instance.save()

			post,_ = Post.objects.get_or_create(message = request.POST.get('message'),
				topic = topic_instance,
				created_by = current_user)
			return redirect('boards:board_topics',pk = board.pk)
		else:
			pass
			
	template = 'boards/new_topic.html'	
	context['board'] = board
	context['form'] = form
	return render(request,template,context)

@login_required
def new_board(request):
	context = dict()
	form = NewBoardForm()
	if request.method == 'POST':
		form = NewBoardForm(request.POST)

		if form.is_valid():
			name = form.cleaned_data["name"]
			description = form.cleaned_data["description"]

			b = Board(name=name, description=description)
			b.save()

			return redirect('/')

		else:
			pass

	template = 'boards/newboard.html'
	context['form'] = form

	return render(request,template,context)

class TopicPostListView(ListView):

	model = Post
	context_object_name = 'posts'
	template_name = 'boards/topic_posts.html'
	paginate_by = 5


	def get_context_data(self,**kwargs):

		session_key = 'viewed_topic_{}'.format(self.topic.pk)

		if not self.request.session.get(session_key,False):
			self.topic.views += 1
			self.topic.save() 
			self.request.session[session_key] = True

		kwargs['topic'] = self.topic
		return super().get_context_data(**kwargs)


	def get_queryset(self):
		self.topic = get_object_or_404(Topic,
			board__pk=self.kwargs.get('board_pk'),
			pk=self.kwargs.get('topic_pk'))

		queryset = self.topic.posts.order_by('-created')
		return queryset

@login_required
def reply_topic(request,board_pk,topic_pk):
    topic = get_object_or_404(Topic,id = topic_pk,board__id = board_pk)
    if request.method == 'POST':
        form = PostForm(data = request.POST)
        if form.is_valid():
            post_instance = form.save(commit=False)
            post_instance.topic = topic
            post_instance.created_by = request.user
            post_instance.save()

            topic.update = timezone.now()
            topic.save()
            # Bug - Fix it !
            return redirect('boards:topic_posts', 
            	board_pk = str(board_pk),
            	topic_pk = str(topic_pk))

        else:
        	pass
    else:
        form = PostForm()
    return render(request, 'boards/reply_topic.html',{'topic': topic, 'form': form})

@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):

	model = Post
	fields = ('message',)
	template_name = 'boards/edit_post.html'
	pk_url_kwarg = 'post_pk'
	context_object_name = 'post'

	def get_queryset(self):
		queryset = super().get_queryset()
		current_user = self.request.user
		user_only_post = queryset.filter(created_by = current_user)
		return user_only_post

	def form_valid(self,form):
		"""
		handling form validation - dev.
		"""
		post = form.save(commit = False)
		post.updated_by = self.request.user
		post.save()
		return redirect('boards:topic_posts', 
            	board_pk = post.topic.board.pk,
            	topic_pk = post.topic.pk)