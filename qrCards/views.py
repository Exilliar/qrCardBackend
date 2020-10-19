from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("qrCards working")


def account(request):
    if request.method == 'GET':
        accountGet(request)
        return HttpResponse("GET")
    elif request.method == 'POST':
        accountPost(request)
        return HttpResponse("POST")
    elif request.method == 'PATCH':
        accountPatch(request)
        return HttpResponse("PATCH")

    return HttpResponse("did not detect request method")


def accountGet(request):
    pass


def accountPost(request):
    pass


def accountPatch(request):
    pass
