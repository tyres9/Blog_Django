from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author' : "Rj",
        'title' : "Blog POst 1",
        "content" : "First post",
        "date_posted" : 'January 29,2024'
    },
        {
        'author' : "KOonyak",
        'title' : "Blog POst 2",
        "content" : "Second post",
        "date_posted" : 'January 30,2024'
    }
]


def home(request):
    context  = {
        "posts" : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html')