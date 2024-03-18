from django.shortcuts import render

# Create your views here.
def index(request):
    return(render(request, 'index.html'))

def admin(request):
    return(render(request, 'admin.html'))

def student(request):
    return(render(request, 'student.html'))

def teacher(request):
    return(render(request, 'teacher.html'))

def contact(request):
    return(render(request, 'contact.html'))
