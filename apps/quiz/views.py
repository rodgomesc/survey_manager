from django.http import HttpResponse
from django.shortcuts import render

''' TODO: implement wizard for questions http://techlaboratory.net/smartwizard or '''
def index(request):
    return render(request, 'quiz/index.html')