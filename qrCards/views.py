from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Stat, CardStats, Card, Account


def index(request):
    return HttpResponse("qrCards working")


@csrf_exempt
def getCards(request, accountid):
    if request.method == 'GET':
        try:
            account = Account.objects.get(pk=accountid)
            cards = list(account.cards.all())
            data = []
            for card in cards:
                stats = list(card.cardStats.all())
                cardObj = {
                    'id': card.pk,
                    'title': card.title,
                    'imgurl': card.imgurl,
                    'stats': []
                }
                for stat in stats:
                    statObj = {
                        'id': stat.pk,
                        'value': stat.value,
                        'name': stat.stat.name
                    }
                    cardObj['stats'].append(statObj)
                data.append(cardObj)

            return JsonResponse(data, safe=False)
        except Account.DoesNotExist:
            return HttpResponse("Account not found", status=400)
        except:
            return HttpResponse("Error in getCards", status=500)
    else:
        return HttpResponse("Only GET allowed", status=405)


@csrf_exempt
def getAccountId(request, accountEmail):
    if request.method == 'GET':
        try:
            account = Account.objects.get(email=accountEmail)
            return JsonResponse({'id': account.pk}, safe=False)
        except Account.DoesNotExist:
            newAccount = Account(email=accountEmail)
            newAccount.save()
            return JsonResponse({'id': newAccount.pk}, safe=False)
        except:
            return HttpResponse("error getting account", status=500)
    else:
        return HttpResponse("Only GET allowed", status=405)


@csrf_exempt
def addCardToAccount(request, accountid, cardid):
    if request.method == 'PATCH':
        try:
            account = Account.objects.get(pk=accountid)
            card = Card.objects.get(pk=cardid)
            account.cards.add(card)
            return HttpResponse("Added card")
        except Account.DoesNotExist:
            return HttpResponse("Account does not exist", status=400)
        except Card.DoesNotExist:
            return HttpResponse("Card does not exist", status=400)
        except:
            return HttpResponse("Error in addCardToAccount", status=500)
    else:
        return HttpResponse("Only PATCH allowed", status=405)
