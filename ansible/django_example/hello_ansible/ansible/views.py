from django.shortcuts import render

def index(request):
    return render(request, 'ansible/index.html')
# Create your views here.
