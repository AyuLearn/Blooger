from django.shortcuts import render
from .models import Contact, Post

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    context ={
        'posts': posts
    }
    return render(request, 'blog.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contacts = Contact(name=name, email=email, subject=subject, message=message)
        contacts.save()
    return render(request, 'contact.html')

def post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context ={
        'post': post
    }
    return render(request, 'post.html', context)