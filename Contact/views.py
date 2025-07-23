from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    
    contac = Contact.objects.filter(name__contains=request.GET.get('search',''))
    contex = {
        'contacts': contac
    }
    return render(request, 'contact/index.html',contex)
@login_required
def view(request, id):
    contac = Contact.objects.get(id=id)
    context = {
        'contact':contac
    }
    return render(request, 'contact/detail.html', context)

#creacion 
@login_required
def create(request):
    if request.method == 'GET':
        form  = ContactForm()
        context = {'form':form}
        return render(request, 'contact/create.html', context)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('contact')

@login_required
def edit(request, id):
    contac = Contact.objects.get(id=id)
    if request.method == 'GET':
        
        form = ContactForm(instance=contac)
        context = {
        'form':form,
        'id': id
        }
        return render(request,'contact/edit.html',context) 
    if(request.method == 'POST'):
        form = ContactForm(request.POST, instance=contac)
        if(form.is_valid()):
            form.save()
        context = {
        'form':form,
        'id': id
        }

        return render(request,'contact/edit.html',context)     

#delete
@login_required
def delete(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('contact')