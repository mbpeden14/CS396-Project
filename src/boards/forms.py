from django import forms
from .import models

class NewTopicForm(forms.ModelForm):
	message = forms.CharField(
		widget=forms.Textarea(attrs={'rows':5,'placeholder':"Type something..."}),
		max_length=250,
		help_text="250 words max.")

	class Meta:
		model  = models.Topic
		fields = ['subject','message']
	 
class PostForm(forms.ModelForm):

	class Meta:
		model = models.Post
		fields = ['message',]

class NewBoardForm(forms.ModelForm):
	name = forms.CharField(max_length=125)
	description = forms.CharField(
		widget=forms.Textarea(attrs={'rows':5,'placeholder':"Type something..."}),
		max_length=250,
		help_text="250 words max.")

	class Meta:
		model = models.Board
		fields = ['name', 'description']