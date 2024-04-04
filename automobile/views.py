from django.shortcuts import render
from django.http import HttpResponse 
from automobile.models import Details
# Create your views here.
def index(request):
    return render (request, "index.html")
def know(request):
    return render (request, "know.html")
def show(request):
    if request.method == "POST":
        show1 = request.POST.get('model')
        posts = Details.objects.filter(model=show1).all()
        data = {
        'posts': posts,
        }
        return render (request, "show.html",data)

