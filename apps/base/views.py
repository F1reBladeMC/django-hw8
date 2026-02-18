from django.shortcuts import render
from apps.base.models import Settings, MyBaseInfo
# Create your views here.
def index(request):
    return render(request, 'index.html', locals())
    
def contact(request):
    return render(request, 'contact-1.html', locals())

def dark_view(request):
    settings = Settings.objects.first()
    base_info = MyBaseInfo.objects.first()
    return render(request, 'dark.html', {'settings': settings, 'base_info': base_info})