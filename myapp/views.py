from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html',{})

def next(request):
    return render(request,'next.html',{})