from django.shortcuts import render,render_to_response
from .models import *
from django import template

# Create your views here.
def index(request):
	return render_to_response('index.html',locals())

def deck(request):
	card_list = card.objects.order_by('cost')
	context={'card_list':card_list}
	return render(request,'deck.html',context)

def card_rank(request):
	return render_to_response('card_rank.html', locals())

def generic(request):
	return render_to_response('generic.html', locals())

