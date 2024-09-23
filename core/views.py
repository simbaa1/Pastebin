
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PasteForm, PASTE_EXPIRY
from .models import Paste, Tag


def set_expirydate(expiry_option):
    today = timezone.now()
    if expiry_option == "tenmins":
        expiry_date = today + timezone.timedelta(minutes=10)
    if expiry_option == "onehour":
        expiry_date = today + timezone.timedelta(hours=1)
    if expiry_option == "oneday":
        expiry_date = today + timezone.timedelta(days=1)
    if expiry_option == "oneweek":
        expiry_date = today + timezone.timedelta(weeks=1)
    if expiry_option == "tenmins":
        expiry_date = today + timezone.timedelta(weeks=2)
    if expiry_option == "tenmins":
        expiry_date = today + timezone.timedelta(weeks=4)
    if expiry_option == "sixmonths":
        expiry_date = today + timezone.timedelta(weeks=24)
    if expiry_option == "oneyear":
        expiry_date = today + timezone.timedelta(days=365)
    else:
        expiry_date = None
    return expiry_date


def home(request):
 
    if request.method == 'POST':
        form = PasteForm(request.POST)
        if form.is_valid():
            paste = form.save(commit=False)

           
            paste_expiry = form.cleaned_data['paste_expiry']
            paste.expiry_date = set_expirydate(paste_expiry)

            paste.save()  

            tag_names = form.cleaned_data['tag_list'].split(',')
            for tag_name in tag_names:
                tag_name = tag_name.strip()
                tag, created = Tag.objects.get_or_create(name=tag_name)
                paste.tags.add(tag) 
            return HttpResponseRedirect(reverse('home'))  
                 
        else:
            print(form.errors)
      
        
    else:
        form = PasteForm()
    context = {
        'form': form
    }
    return render(request, "pages/home.html", context)


def show_pastes(request):
    pastes = Paste.objects.exclude(paste_exposure='PR').order_by('-date_created')[:20]
    context = {
        'pastes' : pastes
    }

    return render(request, "pages/paste_list.html", context)


def paste_detail(request, slug):
    paste = get_object_or_404(Paste, slug=slug)
    tags = paste.tags.all()
    return render(request, 'pages/paste_detail.html', {"paste": paste, "tags": tags})