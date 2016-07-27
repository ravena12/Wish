from django.shortcuts import render, redirect
from .models import User, UserManager, Wish, WishManager
from django.contrib  import messages
import datetime
from django.core.urlresolvers import reverse


####################################################

# PROCESSING DATA 

####################################################

def processregister(request):
	results = User.userManager.isValidReg(request.POST)
	errors = results[1]
	for error in errors:
		messages.error(request, error)
	if results[0]:
		return redirect(reverse('my_travel_index'))
	else: 
		return redirect(reverse('my_wish_register'))

def processlogin(request):
	results = User.userManager.validlog(request.POST)
	print request.POST['username']
	if results[0]:
		request.session['id'] = results[1].id
		print request.session['id']
		
		request.session['username'] = results[1].username

		request.session['first_name'] = results[1].first_name

		return redirect(reverse('my_wish_home'))
	else: 
		errors = results[1]
		for error in errors:
			messages.warning(request, error)
		return redirect(reverse('my_travel_index'))

def processwish(request):
	userid = User.objects.get(id= request.session['id'])
	results = Wish.wishManager.isvalidwish(request.POST, userid)
	Wish.wishManager.create(item = request.POST['item'], creator = User.objects.get(id= request.session['id']))
	return redirect(reverse('my_wish_home'))








####################################################

# DISPLAY PAGES SECTION  

####################################################

def index(request):
	return render(request, 'BBTemp/index.html')


def home(request):
	user = User.objects.get(id=request.session["id"])
	print user
	print Wish.objects.all()
	context = {
		'current': User.objects.get(id=request.session["id"]),
		'thisuser':Wish.objects.filter(creator = user)| Wish.objects.filter(others=user.id),
		'oneu': Wish.objects.filter(creator=user),
		'wishes': Wish.objects.all(),
		'others': Wish.objects.exclude(creator = user.id)
	}
	print Wish.objects.all()

	return render(request, 'BBTemp/home.html',context)

def register(request):
	return render(request, 'BBTemp/registration.html')

def userProfile(request, id):
	context = {
	'person': User.objects.get(id = id)
	}
	return render(request, 'BBTemp/userProfile.html',context)

def destroy(request, id):
	user = User.objects.get(id=request.session["id"]) 
	wish = Wish.objects.get(id =id)
	user = User.objects.get(id=request.session['id'])
	wish.others.remove(user)
	return redirect(reverse('my_wish_home'))

def delete(request, id):
	user = User.objects.get(id=request.session["id"]) 
	item = Wish.objects.get(id = id)
	test = Wish.objects.filter(creator = user)
	item.delete()
	return redirect(reverse('my_wish_home'))

def pedit(request, id):
	update = User.objects.get(id = id)
	update.first_name = request.POST['first_name']
	update.last_name = request.POST['last_name']
	update.username = request.POST['username']
	update.save()
	return redirect(reverse('my_wish_home'))

def join(request, id):
	wish = Wish.objects.get(id =id)
	user = User.objects.get(id=request.session['id'])
	wish.others.add(user)
	return redirect(reverse('my_wish_home'))

def createproduct(request):
	return render(request, 'BBTemp/add.html')

def product(request, id):
	user = User.objects.get(id=request.session["id"])
	context =  {
		'wishes': Wish.objects.get(id = id),
		'others': Wish.objects.exclude(creator = user.id)

	}
	print Wish.objects.get(id = id)
	return render(request, 'BBTemp/product.html', context)

 
def logout(request):
	request.session.clear()
	return redirect(reverse('my_travel_index'))

