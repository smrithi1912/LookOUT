from django.shortcuts import render, HttpResponse, redirect
from forms import FormQuery
from django.shortcuts import render
from django.template import loader
from . import *

def index(request):
    return render(request, 'index.html')

def search(request):
    if request.method=='POST':
        form=FormQuery(request.POST)
        data=form.cleaned_data
        value=data['query']
        if form.is_valid():
            return redirect('Home')
            # try:
            #     album1 = Album.objects.get(artist__contains=value)

            #     return render(request,'Search/form.html',{'album':album1})
            # except:
            #     raise Http404("Does not exist.")
    else:
        return render(request,'index.html')

   
#         if result == '':
#             return redirect('Home')
#         else:
#             return render(request,'results.html',{'google': google_data, 'yahoo': yahoo_data, 'duck': duck_data, 'ecosia': ecosia_data,'bing': bing_data, 'givewater': givewater_data})