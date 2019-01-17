from django.shortcuts import render, HttpResponse, redirect
from random import randrange
from time import strftime
from datetime import datetime

def index(request):
	print("this is the INDEX")
	# print(request.session['total_gold'])
	if 'total_gold' not in request.session:
		request.session['total_gold']= 0
		request.session['activity']=[]
	return render(request, 'gold_app/index.html')

def process_money(request):
	print("this is process!")
	print (request.POST)
	location= request.POST['location']
	
	context={
		'farm': {'min': 10, 'max': 20},
    	'cave': {'min': 5, 'max': 10},
    	'house': {'min': 2, 'max': 5},
    	'casino': {'min': -50, 'max': 50}
	}
	
	print(location)
	range_max = context[location]['max']
	range_min = context[location]['min']
	rand_gold = randrange(range_min, range_max + 1)

	current_time = datetime.now().strftime("%Y-%m-%d %I:%M%p")

	if rand_gold <0:
		sentence = f"Lost {rand_gold * -1} from the {location}.({current_time})"
		color='red'
		
	else:
		sentence = f"Earned {rand_gold} from the {location}! ({current_time})"
		color= 'green'
	
	outcome={
		"description" : sentence,
		"color": color
	}
	request.session['total_gold'] += rand_gold
	request.session['activity'].insert(0, outcome)
	return redirect('/')

def reset(request):
	request.session.clear()
	print("im in reset")
	return redirect('/')

