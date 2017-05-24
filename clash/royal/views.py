from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.
def index(request):
	return render_to_response('index.html',locals())

@csrf_exempt
def deck(request):
	if request.method == "POST":
		if request.POST['action']=="todeck":
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
	context={'card_list':card_list}
	return render(request, 'deck.html', context)


def card_rank(request):
	return render_to_response('card_rank.html', locals())

def generic(request):
	return render_to_response('generic.html', locals())