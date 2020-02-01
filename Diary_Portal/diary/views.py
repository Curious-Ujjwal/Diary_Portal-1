from django.shortcuts import render
from .models import company
# Create your views here.
def gethomepage(request):
    list = company.objects.all()
    return render(request,'diary/base.html',{'company':list})