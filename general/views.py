from django.shortcuts import render

# Create your views here.
def homepage (request):
  return render (request, 'general/index.html')
def about (request):
  return render (request, 'general/about.html')
def service (request):
  return render (request, 'general/services.html')
def contact (request):
  return render (request, 'general/contact.html')
def gallery_single (request):
  return render (request, 'general/gallery-single.html')
def gallery (request):
  return render (request, 'general/gallery.html')
