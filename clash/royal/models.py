from django.db import models

# Create your models here.
class UpdateInfo(models.Model):
	update_date = models.DateField('date published')
	title = models.CharField(max_length=20)
	content = models.TextField(blank=True)
	ImgUrl = models.URLField(blank=True)
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
	def __str__(self):
		return self.idName