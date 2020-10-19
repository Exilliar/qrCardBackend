from django.db import models


class Stat(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CardStats(models.Model):
    value = models.CharField(max_length=50)
    stat = models.ForeignKey(Stat, on_delete=models.CASCADE)


class Card(models.Model):
    title = models.CharField(max_length=200)
    imgurl = models.CharField(max_length=200)
    cardStats = models.ManyToManyField(CardStats)

    def __str__(self):
        return self.title


class Account(models.Model):
    email = models.EmailField()
    cards = models.ManyToManyField(Card)

    def __str__(self):
        return self.email
