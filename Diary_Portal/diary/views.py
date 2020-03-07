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
            remarks(company=c,remark=c.TopRemark,CPOC=c.CPOC,POC=c.POC).save()
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
            remarks(company=c,remark=c.TopRemark,CPOC=c.CPOC,POC=c.POC).save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = forms.add_company()
        return render(request,'diary/add_company.html',{'form':form})

def searchPlacement(request):
    print('I m Here')
    if request.method == 'POST':
        print("success")
        search_text = request.POST['search_text1']
        all_company =(company.objects.filter(CompanyName__contains=search_text)|company.objects.filter(POC__contains=search_text))
        temp = all_company
        for c in all_company:
            if c.placement == False:
                temp = temp.exclude(pk=c.pk)
        return render(request, 'diary/ajax_results1.html', {'all_company': temp})
    else:
        print("fail")
        search_text = ''
        all_company = company.objects.all()
        temp = all_company
        for c in all_company:
            if c.placement == False:
                temp = temp.exclude(pk=c.pk)
        return render(request, 'diary/ajax_results1.html', {'all_company': temp})


def searchIntern(request):
    print('I m Here')
    if request.method == 'POST':
        print("success")
        search_text = request.POST['search_text2']
        all_company = (company.objects.filter(CompanyName__contains=search_text) | company.objects.filter(POC__contains=search_text))
        temp = all_company
        for c in all_company:
            if c.placement == True:
                temp = temp.exclude(pk=c.pk)
        return render(request, 'diary/ajax_results2.html', {'all_company': temp})
    else:
        print("fail")
        search_text = ''
        all_company = company.objects.all()
        temp = all_company
        for c in all_company:
            if c.placement == True:
                temp = temp.exclude(pk=c.pk)
        return render(request, 'diary/ajax_results2.html', {'all_company': temp})


list_globals = globals()
list_globals['Placement_Username'] = "CCD1"
list_globals['Placement_Password'] = "pass1"
list_globals['Intern_Username'] = "CCD2"
list_globals['Intern_Password'] = "pass2"


def Placement_Authenticate(request):
    if request.method=="POST":
        form = forms.authentication(request.POST)
        if form.is_valid():
            if list_globals['Placement_Username']==form.cleaned_data['Username'] and list_globals['Placement_Password']==form.cleaned_data['Password']:
                return getPlacement(request)
            else:
                form = forms.authentication()
                return render(request,'diary/Auth.html',{'form':form})
        else:
            form = forms.authentication()
            return render(request, 'diary/Auth.html', {'form': form})
    else:
        form = forms.authentication()
        return render(request, 'diary/Auth.html', {'form': form})

def Intern_Authenticate(request):
    if request.method=="POST":
        form = forms.authentication(request.POST)
        if form.is_valid():
            if list_globals['Intern_Username']==form.cleaned_data['Username'] and list_globals['Intern_Password']==form.cleaned_data['Password']:
                return getIntern(request)
            else:
                form = forms.authentication()
                return render(request, 'diary/Auth.html', {'form': form})
        else:
            form = forms.authentication()
            return render(request, 'diary/Auth.html', {'form': form})
    else:
        form = forms.authentication()
        return render(request, 'diary/Auth.html', {'form': form})



def edit_Placement_ID(request):
    if request.method=="POST":
        form = forms.change_username_password(request.POST)
        if form.is_valid():
            if list_globals['Placement_Username']==form.cleaned_data['Current_Username'] and list_globals['Placement_Password']==form.cleaned_data['Current_Password']:
                if form.cleaned_data['New_Password'] == form.cleaned_data['Confirm_Password']:
                    list_globals['Placement_Username'] = form.cleaned_data['New_Username']
                    list_globals['Placement_Password'] = form.cleaned_data['New_Password']
                    return getPlacement(request)
                else:
                    form = forms.change_username_password()
                    return render(request,'diary/edit_ID.html',{'form':form})
            else:
                form = forms.change_username_password()
                return render(request, 'diary/edit_ID.html', {'form': form})
        else:
            form = forms.change_username_password()
            return render(request, 'diary/edit_ID.html', {'form': form})
    else:
        form = forms.change_username_password()
        return render(request, 'diary/edit_ID.html', {'form': form})


def edit_Intern_ID(request):
    if request.method=="POST":
        form = forms.change_username_password(request.POST)
        if form.is_valid():
            if list_globals['Intern_Username']==form.cleaned_data['Current_Username'] and list_globals['Intern_Password']==form.cleaned_data['Current_Password']:
                if form.cleaned_data['New_Password'] == form.cleaned_data['Confirm_Password']:
                    list_globals['Intern_Username'] = form.cleaned_data['New_Username']
                    list_globals['Intern_Password'] = form.cleaned_data['New_Password']
                    return getPlacement(request)
                else:
                    form = forms.change_username_password()
                    return render(request,'diary/edit_ID.html',{'form':form})
            else:
                form = forms.change_username_password()
                return render(request, 'diary/edit_ID.html', {'form': form})
        else:
            form = forms.change_username_password()
            return render(request, 'diary/edit_ID.html', {'form': form})
    else:
        form = forms.change_username_password()
        return render(request, 'diary/edit_ID.html', {'form': form})

