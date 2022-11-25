from django.shortcuts import render

# Create your views here.

def a1_second(request):
    d={'a':8787}
    return render(request,'a1_second.html',d)