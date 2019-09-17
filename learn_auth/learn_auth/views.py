from django.shortcuts import render

def index(request):
    return render(request, 'basic_auth/index.html')