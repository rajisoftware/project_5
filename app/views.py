from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':20 ,'b':50,'c':30}
    return render(request,'conditions.html',d)
def loops(request):
    d={'name':'raj'}
    return render(request,'loops.html',d)
