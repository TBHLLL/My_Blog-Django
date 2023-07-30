from django import forms
from django.forms import ModelForm,FileInput
from .models import File

class UploadFileForm(ModelForm):
    class Meta:
        model = File
        fields = "__all__"