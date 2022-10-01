from django import forms
from .models import *
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {'main_img':""}