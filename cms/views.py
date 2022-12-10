from django.shortcuts import render
from .models import *
# Create your views here.
def home(r):
    data = {}
    data['category'] = Category.objects.all()
    data['posts'] = Post.objects.all()
    return render(r,"home.html",data)

def insert(r):
    if r.method == "POST":
        return

    return render(r,"insert.html")