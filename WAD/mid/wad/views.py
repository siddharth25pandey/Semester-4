from django.shortcuts import render,redirect,reverse
from django.conf import settings
from . import forms,models
def home_view(request):
    return render(request,'wad/index.html')
def home_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            name=sub.cleaned_data['Name']
            roll=sub.cleaned_data['Roll']
            branch=sub.cleaned_data['Branch']
            college=sub.cleaned_data['College']
            max_sub=sub.cleaned_data['Max_sub']
            sub1=sub.cleaned_data['Sub1']
            sub2=sub.cleaned_data['Sub2']
            sub3=sub.cleaned_data['Sub3']
            sub4=sub.cleaned_data['Sub4']
            sub5=sub.cleaned_data['Sub5']
            return render(request, 'wad/index.html')
        return render(request, 'wad/index.html', {'form':sub})