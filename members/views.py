from  django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def memb(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def form(request):
    return HttpResponse("Hi")



def full(request, name = 'tushar' ):
    name = input("enter ypur name: {name}" )
    return HttpResponse(f"Hi {name}")

def fullname(request):
    return HttpResponse("name")


def coupenCode(request):
    return HttpResponse("your is code: XSDNE27")

def code(requst):
    template = loader.get_template('formElement.html')
    return HttpResponse(template.render())

def feb(request):
    template = loader.get_template('formElement.html')
    return HttpResponse(template.render())

def myself(request):
    template = loader.get_template('Author.html')
    return HttpResponse(template.render())


def formInput(request):
   return HttpResponse('Nothing')

def companyAbout(requests):
    template = loader.get_template("CompanyAbout.html")
    return HttpResponse(template.render())


def sept(request):
    template = loader.get_template('sept.html')
    return HttpResponse(template.render())
def oct(request):
    template = loader.get_template('oct.html')
    return HttpResponse(template.render())
def nov(request):
    template = loader.get_template('nov.html')
    return HttpResponse(template.render())
def dec(request):
    template = loader.get_template('dec.html')
    return HttpResponse(template.render())