from django.shortcuts import render
from .models import Link

# Create your views here.
def list(request):
    links = Link.objects.all()
    return render(request, 'links/link_list.html', {
        'links':links
    })