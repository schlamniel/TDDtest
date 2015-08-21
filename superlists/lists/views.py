from django.shortcuts import render, redirect
from django.http import HttpResponse

from lists.models import Item
# Create your views here.

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', locals())

def home_page(request):
    return render(request, 'home.html', locals())

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')
