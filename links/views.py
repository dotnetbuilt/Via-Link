from django.shortcuts import render, redirect
from .models import Link
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def list(request):
    links = Link.objects.all()
    return render(request, 'links/link_list.html', {
        'links':links
    })

def detail(request, pk):
    link = Link.objects.get(pk=pk)
    return render(request, 'links/link_detail.html', {
        'link': link
    })

@login_required(login_url="/accounts/login/")
def new_link(request):
    if request.method == 'POST': 
        form = forms.LinkForm(request.POST, request.FILES) 
        if form.is_valid():
            newlink = form.save(commit=False) 
            newlink.author = request.user 
            newlink.save()
            return redirect('links:list')
    else:
        form = forms.LinkForm()
    return render(request, 'links/new_link.html', { 'form': form })