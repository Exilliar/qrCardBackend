from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Stat, CardStats, Card, Account

# Create your views here.


def index(request):
    return HttpResponse("qrCards working")


@csrf_exempt
def card(request, accountid):
    if request.method == 'GET':
        return getCards(accountid)
    else:
        return HttpResponse(status=405)


def getCards(accountid):
    try:
        account = Account.objects.get(pk=accountid)
        cards = list(account.cards.all())
        data = []
        for card in cards:
            stats = list(card.cardStats.all())
            cardObj = {
                'title': card.title,
                'imgurl': card.imgurl,
                'cardStats': []
            }
            for stat in stats:
                statObj = {
                    'value': stat.value,
                    'name': stat.stat.name
                }
                cardObj['cardStats'].append(statObj)
            data.append(cardObj)

        return JsonResponse(data, safe=False)
    except:
        return HttpResponse("account not found")


def account(request):
    if request.method == 'GET':
        return accountGet(request)
    elif request.method == 'POST':
        accountPost(request)
        return HttpResponse("POST")
    elif request.method == 'PATCH':
        accountPatch(request)
        return HttpResponse("PATCH")

    return HttpResponse("did not detect request method")


def accountGet(request):
    try:
        accountData = Account.objects.get(email="test@test.com")
        return HttpResponse(accountData)
    except:
        return HttpResponse("could not find account")


def accountPost(request):
    pass


def accountPatch(request):
    pass
