from django.db import models


class Account(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Card(models.Model):
    title = models.CharField(max_length=200)
    imgurl = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Stat(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AccountCards(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)


class CardStats(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    stat = models.ForeignKey(Stat, on_delete=models.CASCADE)
