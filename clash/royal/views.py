from __future__ import division
from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from .models import *

# Create your views here.
def index(request):
	return render_to_response('index.html',locals())

@csrf_exempt
def deck(request):
	if request.method == "POST":
		checkdeck = CardInfo.objects.order_by('elixirCost')
		currentDeck = []
		if request.POST['action']=="todeck":
			for cards in checkdeck:
				if cards.inDeck:
					currentDeck.append(cards.id)
			if len(currentDeck)<8:
				value=request.POST.get("value")
				b=CardInfo.objects.get(id=str(value))
				b.inDeck=True
				b.save()
		if request.POST['action']=="outdeck":
			value=request.POST.get("value")
			b=CardInfo.objects.get(id=str(value))
			b.inDeck=False
			b.save()
	card_list = CardInfo.objects.order_by('elixirCost')
	cost=0
	Deck=[]
	for deckcard in card_list:
		if deckcard.inDeck:
			cost+=deckcard.elixirCost
			Deck.append(deckcard)
	if len(Deck)>0:
		averagecost=float(cost) /len(Deck)
		averagecost=round(averagecost, 2)
	else:
		averagecost=0
	form = DeckForm()
	context={'card_list':card_list,'averagecost':averagecost,'form':form}
	return render(request, 'deck.html', context)


def card_rank(request):
	return render_to_response('card_rank.html', locals())

def generic(request):
	card_list =  CardInfo.objects.order_by('idName')
	context = {'card_list':card_list}
	return render(request, 'generic.html', context)
