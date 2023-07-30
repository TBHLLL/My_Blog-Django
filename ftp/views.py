from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .forms import UploadFileForm

class file_update(View):
    def get(self,request):
        form = UploadFileForm(request.POST,request.FILES)
        return render(request,'file/upload.html',{ 'form':form })
    def post(self,request):
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
class file_download(View):
    pass
