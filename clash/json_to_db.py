import os
os.environ.update({"DJANGO_SETTINGS_MODULE": "clash.settings"})
import json
import django
django.setup()
from django.db import models
from royal.models import CardInfo

with open("clash.json") as json_file:
	json_data = json.load(json_file)

for data in json_data:
	ci = CardInfo(
	idName = data['idName'],
	rarity = data['rarity'],
	type = data['type'],
	name = data['name'],
	description = data['description'],
	arena = data['arena'],
	elixirCost = data['elixirCost']
	)
	ci.save()