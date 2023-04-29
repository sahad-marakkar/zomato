from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'zomato1/index.html')

def home(request):
    return render(request,'zomato1/grid.html')

def sahad(request):
    return render(request,'zomato1/flex.html')

def boot(request):
    return render(request,'zomato1/bootstrap.html')


def javascript(request):
    return render(request,'zomato1/javascript.html')

def conditions(request):
    return render(request,'zomato1/conditions-loops.html')


def boot2(request):
    return render(request,'zomato1/bootstrap2.html')

def try1(request):
    return render(request,'zomato1/try.html')

def dome(request):
    return render(request,'zomato1/dome.html')


def dom1(request):
    return render(request,'zomato1/dom1.html')

def calc(request):
    return render(request,'zomato1/calculator.html')