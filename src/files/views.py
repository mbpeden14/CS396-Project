from django.shortcuts import render, redirect
from .forms import *
from .models import MyFileUpload
from django.contrib import messages
import os
from boards import *

# Imaginary function to handle an uploaded file.
def filesdata(response):
    data = MyFileUpload.objects.all()
    return render(response, "filestorage.html", {"data":data})

def home(request):
    mydata=MyFileUpload.objects.all()    
    myform=MyFileForm()
    if mydata!='':
        context={'form':myform,'mydata':mydata}
        return render(request,'filestorage.html',context)
    else:
        context={'form':myform}
        return render(request,"filestorage.html",context)

def uploadfile(request):
    if request.method=="POST":
        myform=MyFileForm(request.POST,request.FILES)

        if myform.is_valid():
            MyFileName = request.POST.get('name') 
            MyFile = request.FILES.get('file')

            exists=MyFileUpload.objects.filter(file=MyFile).exists()

            if exists:
                messages.error(request,'%s already exists'% MyFile)
            else:
                MyFileUpload.objects.create(name=MyFileName,file=MyFile).save()
                messages.success(request,"File uploaded successfully.")
                
        return redirect('../upload/')

def deleteFile(request,id):
    mydata=MyFileUpload.objects.get(id=id)    
    mydata.delete()    
    os.remove(mydata.file.path)
    messages.success(request,'File deleted successfully.')  
    return redirect('../upload/')

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/files')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})