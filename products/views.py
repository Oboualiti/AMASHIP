from django.shortcuts import render,redirect
from products.models import Products,Email

import json

def index(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        data=Email(email=email)
        data.save() 
        return redirect('/done')   
    return render(request, 'index.html', {'pro' : Products.objects.all()})

def done(request):
    return render(request, 'done_demande.html', {'done':'done'})

def product_detial(request , id):
    product_detail=Products.objects.get(id=id)
    if request.method == 'POST':
        email=request.POST.get('email')
        data=Email(email=email)
        data.save() 
        return redirect('/done') 
      
    return render(request, 'products_details.html',{'prod':product_detail, 'pro':Products.objects.all()})

def conditions(request):
    return render(request,'conditions_general.html' , {'conditions':'conditions'})

def contact(request):
    return   render(request,'contact_us.html',{'contact':'contact'})

def private(request):
    return render(request,'private_policy.html',{'private':'private'}) 



    