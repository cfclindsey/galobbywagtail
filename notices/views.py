from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('Welcome to GA Lobby')
    return render(request, 'notices/base.html')

def create_notice(request):
    return render(request, 'notices/createnotice.html')
