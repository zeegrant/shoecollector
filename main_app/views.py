from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Shoe, Sock
from .forms import StorageForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def shoes_index(request):
  shoes = Shoe.objects.all()  
  return render(request, 'shoes/index.html', { 'shoes': shoes})

def shoes_detail(request, shoe_id):
  shoe = Shoe.objects.get(id=shoe_id)
  id_list = shoe.socks.all().values_list('id')
  socks_shoe_doesnt_have = Sock.objects.exclude(id__in=id_list)  
  storage_form = StorageForm()
  return render(request, 'shoes/detail.html', { 
    'shoe': shoe, 
    'storage_form': storage_form,
    'socks': socks_shoe_doesnt_have
  })

def add_storage(request, shoe_id):
  form = StorageForm(request.POST)
  if form.is_valid():
    new_storage = form.save(commit=False)
    new_storage.shoe_id = shoe_id
    new_storage.save()
  return redirect('detail', shoe_id=shoe_id) 

def assoc_sock(request, shoe_id, sock_id):
  Shoe.objects.get(id=shoe_id).socks.add(sock_id)
  return redirect('detail', shoe_id=shoe_id)
 

class ShoeCreate(CreateView):
    model = Shoe
    fields = ['designer', 'style', 'description', 'size' ]
    # success_url = '/shoes/'
    

class ShoeUpdate(UpdateView):
    model = Shoe
    fields = ['style', 'description', 'size']
    
class ShoeDelete(DeleteView):
    model = Shoe
    success_url  = '/shoes/'


class SockList(ListView):
  model = Sock

class SockDetail(DetailView):
  model = Sock

class SockCreate(CreateView):
  model = Sock
  fields = '__all__'

class SockUpdate(UpdateView):
  model = Sock
  fields = ['type', 'color']

class SockDelete(DeleteView):
  model = Sock
  success_url = '/socks/'