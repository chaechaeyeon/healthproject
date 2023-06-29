from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")


def meaningPage(request):
    return render(request,"information\meaning.html")

def effectPage(request):
    return render(request,"information\effect.html")

def cautionPage(request):
    return render(request,"information\caution.html")

def contactPage(request):
    return render(request,"contact.html")

def recommendPage(request):
    return render(request,"recommend.html")

