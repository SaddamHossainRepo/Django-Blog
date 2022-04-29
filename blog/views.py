from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'coreyMS',
        'title': "Blog post 1",
        'content': 'first post content',
        'date_posted': 'April 20, 2022'
    },
    {
        'author': 'John Doe',
        'title': "Blog post 2",
        'content': 'second post content',
        'date_posted': 'April 22, 2022'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

