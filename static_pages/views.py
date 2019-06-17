from django.shortcuts import render

# Create your views here.

def about(request):
    template='static_pages/about.html'

    return render(request,template)

def contact(request):
    template='static_pages/contact.html'

    return render(request,template)

