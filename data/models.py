from django.db import models
from django.urls import reverse
from datetime import datetime,date
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
	
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True,blank=True)

	def __str__(self):
		return self.name

class gamedata(models.Model):
	gamename = models.CharField(max_length=264)
	description= models.TextField()
	post_image = models.ImageField(null=True,blank=True,upload_to='pictures/')
	# bgimage = models.ImageField(null=True,blank=True,upload_to='bgpictures/')
    # preownedprice = models.IntegerField(blank=True,null=True)
	gamenum = models.IntegerField(blank=True,null=True)
	newgameprice = models.FloatField(blank=True,null=True)
	platform = models.CharField(max_length=100)

	def __str__(self):
		return self.gamename

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	# @property
	# def shipping(self):
	# 	shipping = False
	# 	orderitems = self.orderitem_set.all()
	# 	for i in orderitems:
	# 		if i.product.digital == False:
	# 			shipping = True
	# 	return shipping
	#

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

class OrderItem(models.Model):
	product = models.ForeignKey(gamedata, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.newgameprice * self.quantity
		return total

