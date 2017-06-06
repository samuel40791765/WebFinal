from __future__ import division
from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from .models import *

# Create your views here.
def index(request):
	return render_to_response('index.html',locals())

@csrf_exempt
def deck(request):
	form = DeckForm(prefix="deck")
	card_list = CardInfo.objects.order_by('elixirCost')
	cost=0
	Deck=[]
	enough=True;
	for deckcard in card_list:
		if deckcard.inDeck:
			cost+=deckcard.elixirCost
			Deck.append(deckcard)
	if len(Deck)>0:
		averagecost=float(cost) /len(Deck)
		averagecost=round(averagecost, 2)
	else:
		averagecost=0
	search=SearchMethod.objects.get(id=1)
	

	if request.method == "POST":
		checkdeck = CardInfo.objects.order_by('elixirCost')
		currentDeck = []
		form = DeckForm(request.POST, prefix="deck")
		if form.is_valid() and len(Deck)== 8:
			deck=form.save(commit=False)
			deck.cost=averagecost
			deck.card1=Deck[0].idName
			deck.card2=Deck[1].idName
			deck.card3=Deck[2].idName
			deck.card4=Deck[3].idName
			deck.card5=Deck[4].idName
			deck.card6=Deck[5].idName
			deck.card7=Deck[6].idName
			deck.card8=Deck[7].idName
			for card in Deck:
				temp=CardInfo.objects.get(id=str(card.id))
				temp.inDeck=False
				temp.save()
			deck.save()
			return redirect('mydecks')
		elif form.is_valid() and len(Deck)!= 8:
			enough=False
		elif request.POST['action']=="todeck":
			for cards in checkdeck:
				if cards.inDeck:
					currentDeck.append(cards.id)
			if len(currentDeck)<8:
				value=request.POST.get("value")
				b=CardInfo.objects.get(id=str(value))
				b.inDeck=True
				b.save()
		elif request.POST['action']=="outdeck":
			value=request.POST.get("value")
			b=CardInfo.objects.get(id=str(value))
			b.inDeck=False
			b.save()
		elif request.POST['action']=="filter":
			search.rarity=request.POST.get("raritySearch")
			search.elixir=request.POST.get("elixirSearch")
			search.arena=request.POST.get("arenaSearch")
			search.typeof=request.POST.get("typeSearch")
			search.save()

	context={'card_list':card_list,'averagecost':averagecost,'form':form,'enough':enough,
	'rarity':search.rarity,'elixir':search.elixir,'arena':search.arena,'typeof':search.typeof}
	return render(request, 'deck.html', context)

def mydecks(request):
	deck_list = Deck.objects.order_by('name')
	card_list = CardInfo.objects.order_by('elixirCost')
	context={'deck_list':deck_list,'card_list':card_list}
	return render(request, 'mydecks.html', context)

@csrf_exempt
def deck_edit(request,pk):
	deck = get_object_or_404(Deck, pk=pk)
	card_list = CardInfo.objects.order_by('elixirCost')
	cost=0
	cards=0
	enough=True;
	search=SearchMethod.objects.get(id=1)
	for deckcard in card_list:
		if deck.card1==deckcard.idName:
			cost+=deckcard.elixirCost
			cards+=1
		elif deck.card2==deckcard.idName:
			cost+=deckcard.elixirCost
			cards+=1
		elif deck.card3==deckcard.idName:
			cost+=deckcard.elixirCost
			cards+=1
		elif deck.card4==deckcard.idName:
			cost+=deckcard.elixirCost
			cards+=1
		elif deck.card5==deckcard.idName:
			cost+=deckcard.elixirCost
			cards+=1
		elif deck.card6==deckcard.idName:
			cost+=deckcard.elixirCost
			cards+=1
		elif deck.card7==deckcard.idName:
			cost+=deckcard.elixirCost
			cards+=1
		elif deck.card8==deckcard.idName:
			cost+=deckcard.elixirCost
			cards+=1

	if request.method == "POST":
		form = DeckForm(request.POST, instance=deck)
		if form.is_valid() and cards==8 and 'action' not in request.POST:
			deck = form.save(commit=False)
			deck.save()
			return redirect('mydecks')
		elif form.is_valid() and cards!=8 and 'action' not in request.POST:
			enough=False
		elif request.POST['action']=="todeck":
			value=request.POST.get("value")
			if deck.card1=='null':
				deck.card1=value
				for deckcard in card_list:
					if deck.card1==deckcard.idName:
						cost+=deckcard.elixirCost
						cards+=1
			elif deck.card2=="null":
				deck.card2=value
				for deckcard in card_list:
					if deck.card2==deckcard.idName:
						cost+=deckcard.elixirCost
						cards+=1
			elif deck.card3=="null":
				deck.card3=value
				for deckcard in card_list:
					if deck.card3==deckcard.idName:
						cost+=deckcard.elixirCost
						cards+=1
			elif deck.card4=="null":
				deck.card4=value
				for deckcard in card_list:
					if deck.card4==deckcard.idName:
						cost+=deckcard.elixirCost
						cards+=1
			elif deck.card5=="null":
				deck.card5=value
				for deckcard in card_list:
					if deck.card5==deckcard.idName:
						cost+=deckcard.elixirCost
						cards+=1
			elif deck.card6=="null":
				deck.card6=value
				for deckcard in card_list:
					if deck.card6==deckcard.idName:
						cost+=deckcard.elixirCost
						cards+=1
			elif deck.card7=="null":
				deck.card7=value
				for deckcard in card_list:
					if deck.card7==deckcard.idName:
						cost+=deckcard.elixirCost
						cards+=1
			elif deck.card8=="null":
				deck.card8=value
				for deckcard in card_list:
					if deck.card8==deckcard.idName:
						cost+=deckcard.elixirCost
						cards+=1
			if cards>0:
				averagecost=float(cost) /cards
				averagecost=round(averagecost, 2)
			else:
				averagecost=0
			deck.cost=averagecost
			deck.save()
		elif request.POST['action']=="outdeck":
			value=request.POST.get("value")
			if deck.card1 == value:
				deck.card1='null'
				for deckcard in card_list:
					if deck.card1==deckcard.idName:
						cost-=deckcard.elixirCost
						cards-=1
			elif deck.card2==value:
				deck.card2="null"
				for deckcard in card_list:
					if deck.card2==deckcard.idName:
						cost-=deckcard.elixirCost
						cards-=1
			elif deck.card3==value:
				deck.card3="null"
				for deckcard in card_list:
					if deck.card3==deckcard.idName:
						cost-=deckcard.elixirCost
						cards-=1
			elif deck.card4==value:
				deck.card4="null"
				for deckcard in card_list:
					if deck.card4==deckcard.idName:
						cost-=deckcard.elixirCost
						cards-=1
			elif deck.card5==value:
				deck.card5="null"
				for deckcard in card_list:
					if deck.card5==deckcard.idName:
						cost-=deckcard.elixirCost
						cards-=1
			elif deck.card6==value:
				deck.card6="null"
				for deckcard in card_list:
					if deck.card6==deckcard.idName:
						cost-=deckcard.elixirCost
						cards-=1
			elif deck.card7==value:
				deck.card7="null"
				for deckcard in card_list:
					if deck.card7==deckcard.idName:
						cost-=deckcard.elixirCost
						cards-=1
			elif deck.card8==value:
				deck.card8="null"
				for deckcard in card_list:
					if deck.card8==deckcard.idName:
						cost-=deckcard.elixirCost
						cards-=1
			if cards>0:
				averagecost=float(cost) /cards
				averagecost=round(averagecost, 2)
			else:
				averagecost=0
			deck.cost=averagecost
			deck.save()
		elif request.POST['action']=="filter":
			search.rarity=request.POST.get("raritySearch")
			search.elixir=request.POST.get("elixirSearch")
			search.arena=request.POST.get("arenaSearch")
			search.typeof=request.POST.get("typeSearch")
			search.save()

	else:
		form = DeckForm(instance=deck)
	
	context={'form': form, 'card_list':card_list,'deck':deck,'enough':enough,
	'rarity':search.rarity,'elixir':search.elixir,'arena':search.arena,'typeof':search.typeof}
	return render(request, 'deck_edit.html', context)

def deck_delete(request,pk):
	deck_list = Deck.objects.order_by('name')
	card_list = CardInfo.objects.order_by('id')
	try:
		deck = Deck.objects.get(pk=pk)
		deck.delete();
		deck_list = Deck.objects.order_by('name')
	except Deck.DoesNotExist:
		context={'deck_list':deck_list,'card_list':card_list}
		return render(request, 'mydecks.html', context)
	context={'deck_list':deck_list,'card_list':card_list}
	return render(request, 'mydecks.html', context)

def card_rank(request):
	return render_to_response('card_rank.html', locals())

def generic(request):
	card_list =  CardInfo.objects.order_by('idName')
	context = {'card_list':card_list}
	return render(request, 'generic.html', context)
