from django.shortcuts import render,render_to_response

# Create your views here.
def index(request):
	return render_to_response('index.html',locals())

def deck(request):
	return render_to_response('deck.html',locals())
