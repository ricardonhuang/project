from django.shortcuts import render
from models import Passage
# Create your views here.
def home(request):
    return render(request,'home.html')
def displaypassage(request):
    content = Passage.objects.all()
        
    return render(request,'passage.html',{'content':content})
