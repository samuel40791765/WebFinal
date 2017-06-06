from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class UpdateInfo(models.Model):
	update_date = models.DateField('date published')
	title = models.CharField(max_length=20)
	content = models.TextField(blank=True)
	shoutcut = models.TextField(max_length=100, default="None")
	ImgUrl = models.CharField(max_length=50)
	ImgName = models.CharField(max_length=20)
	def __str__(self):
		return self.title


class CardInfo(models.Model):
	idName = models.CharField(max_length=20)
	rarity = models.CharField(max_length=20)
	type = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	description = models.TextField(max_length=200)
	arena = models.IntegerField()
	elixirCost = models.IntegerField()
	inDeck = models.BooleanField(default=False)
	def __str__(self):
		return self.idName

class SearchMethod(models.Model):
	rarity=models.CharField(max_length=20,default="None")
	typeof=models.CharField(max_length=20,default="None")
	elixir=models.IntegerField(default=0)
	arena=models.IntegerField(default=-1)


class Deck(models.Model):
	cost=models.FloatField()
	name=models.CharField(max_length=20)
	description = models.TextField(max_length=200)
	card1=models.CharField(max_length=20)
	card2=models.CharField(max_length=20)
	card3=models.CharField(max_length=20)
	card4=models.CharField(max_length=20)
	card5=models.CharField(max_length=20)
	card6=models.CharField(max_length=20)
	card7=models.CharField(max_length=20)
	card8=models.CharField(max_length=20)
	def __str__(self):
		return self.name