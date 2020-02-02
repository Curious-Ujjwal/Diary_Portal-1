from django.shortcuts import render
from .models import company,remarks
# Create your views here.
def gethomepage(request):
    list = company.objects.all()
    return render(request,'diary/base.html',{'company':list})


def getremarks(request,pk):
    c = company.objects.get(pk=pk)
    remark = remarks.objects.all()
    final =[]
    for r in remark:
        if r.company.CompanyName == c.CompanyName:
            final.append(r)
    return render(request,'diary/company_remarks.html',{'remark':final})


