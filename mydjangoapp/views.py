from django.shortcuts import render
from django.http import HttpResponse
from . import forms

from mydjangoapp.models import Accesspage,Webpage,Topic

def form_view(request):
    form = forms.forname
    
    if request.method=="POST":
        form = forms.forname(request.POST)

        if form.is_valid():
            print("Validation success!")
            print('Name: ' + form.cleaned_data['name'])
            print('E-mail: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])
    return render(request, 'mydjangoapp/form_page.html',{'form':form})

def index(request):
    my_dir={'inside_me':"Appearing from the django edited text!"}
    return render(request,'mydjangoapp/index.html',context=my_dir)
    

def info(request):
    Webpagelist = Accesspage.objects.order_by('date')
    date_dir={'access_records': Webpagelist}
    return render(request, 'mydjangoapp/info.html',context=date_dir)

def help(request):
    form = forms.newForm
    
    if request.method=="POST":
        form = forms.newForm(request.POST)

        if form.is_valid():
            print("Validation success!")
            form.save(commit=True)
            return index(request)
    return render(request, 'mydjangoapp/help.html',{'form':form})

def users(request):
    company = Webpage.objects.all()
    company_dir={'companies':company}
    return render(request, 'mydjangoapp/users.html',context=company_dir)