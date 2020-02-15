from django.shortcuts import render
from .models import company,remarks
from django.http import HttpResponseRedirect
from . import forms
# Create your views here.
def getPlacement(request):
    list = company.objects.all()
    final1 = []
    for r in list:
        if r.placement == True:
            final1.append(r)
    return render(request,'diary/placement_base.html',{'company':final1})

def getIntern(request):
    list = company.objects.all()
    final1 = []
    for r in list:
        if r.placement == False:
            final1.append(r)
    return render(request,'diary/intern_base.html',{'company':final1})

def placement_edit(request,cpk):
    c = company.objects.get(pk=cpk)
    final1 = []
    final1.append(c);
    return render(request, 'diary/edit_company.html', {'company': final1})

def getmainpage(request):
    return render(request,'diary/placement_or_intern.html')


def getremarks(request,pk):
    c = company.objects.get(pk=pk)
    remark = remarks.objects.all()
    final =[]
    for r in remark:
        if r.company == c:
            final.append(r)
    final.reverse()
    return render(request,'diary/company_remarks.html',{'remark':final})


def save_changes_view(request,pk):
    c = company.objects.get(pk=pk)
    if request.method=='POST':
        form = forms.save_changes(request.POST)
        if form.is_valid():
            poc = form.cleaned_data['POC']
            cpoc = form.cleaned_data['CPOC']
            remark = form.cleaned_data['Remark']
            c.CPOC = cpoc
            c.POC  = poc
            c.TopRemark = remark
            c.save()
            print(poc+" "+cpoc+" "+remark)
            remarks(company=c,remark=remark,CPOC=cpoc).save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = forms.save_changes()
        return render(request,'diary/edit_company.html',{'form':form,'c':c})


def add_placement_company(request):
    if request.method=='POST':
        form = forms.add_company(request.POST)
        if form.is_valid():
            c = company()
            c.CompanyName = form.cleaned_data['CompanyName']
            c.POC = form.cleaned_data['POC']
            c.CPOC = form.cleaned_data['CPOC']
            c.placement = True
            c.TopRemark = form.cleaned_data['Remark']
            c.save()
            remarks(company=c,remark=c.TopRemark,CPOC=c.CPOC).save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = forms.add_company()
        return render(request,'diary/add_company.html',{'form':form})

def add_intern_company(request):
    if request.method=='POST':
        form = forms.add_company(request.POST)
        if form.is_valid():
            c = company()
            c.CompanyName = form.cleaned_data['CompanyName']
            c.POC = form.cleaned_data['POC']
            c.CPOC = form.cleaned_data['CPOC']
            c.placement = False
            c.TopRemark = form.cleaned_data['Remark']
            c.save()
            remarks(company=c,remark=c.TopRemark,CPOC=c.CPOC).save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = forms.add_company()
        return render(request,'diary/add_company.html',{'form':form})
