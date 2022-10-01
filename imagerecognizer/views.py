from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Image
from .forms import ImageForm
from django.views.decorators.csrf import csrf_exempt

def index(request):    
    return render(request, "imagerecognizer/index.html",{"image_form":ImageForm})
@csrf_exempt 
def upload_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image_obj=form.save()
            uploaded_image_url=uploaded_image_obj.main_img.url
    return JsonResponse({"uploaded_image":uploaded_image_url})