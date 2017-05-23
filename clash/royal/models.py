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

class card(models.Model):
	RARITY_CHOICES = (
    	('C', 'Common'),
    	('R', 'Rare'),
    	('E', 'Epic'),
    	('L', 'Legendary'),
	)
	TYPE_CHOICES = (
    	('T', 'Troop'),
    	('S', 'Spell'),
    	('B', 'Building'),
	)
	name=models.CharField(max_length=20,blank=False)
	rarity=models.CharField(max_length=20,choices=RARITY_CHOICES,blank=False)
	cost=models.PositiveIntegerField(blank=False)
	arena=models.PositiveIntegerField(blank=False)
	cardtype=models.CharField(max_length=20,choices=TYPE_CHOICES,blank=False)
	ImgUrl=models.CharField(max_length=30,blank=True)
	def __str__(self):
		return self.name
