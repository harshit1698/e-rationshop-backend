from django.db import models
from django.conf import settings

# Create your models here.

class Role_table(models.Model):
    role_name = models.CharField(max_length=20)

    def __str__(self):
        return self.role_name

class Account_table(models.Model):
    auth_id = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role_table, to_field='id', on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    contact = models.CharField(max_length=10)

    def __str__(self):
        return str(self.auth_id)

class Region_table(models.Model):
    region_name = models.CharField(max_length=50)
    pin = models.IntegerField()    
    is_open=models.BooleanField(default=True) #for new Recruitment
    

    def __str__(self):
        return str(self.region_name)+" "+str(self.pin)

class Shop_table(models.Model):
    shopkeeper_id = models.ForeignKey(Account_table, to_field='id', on_delete=models.CASCADE)
    region_id = models.ForeignKey(Region_table, to_field='id', on_delete=models.CASCADE)
    noti_flag = models.BooleanField()
    address = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=10)
    is_blocked = models.BooleanField(default=False)
    is_requested= models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(str(self.region_id))

class History_table(models.Model):
    month = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return "month {} year {}".format(self.month,self.year)


class Global_item_table(models.Model):
    History_id = models.ForeignKey(History_table, to_field='id', on_delete=models.CASCADE,default=None)
    item_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    remaining = models.IntegerField()
    price = models.FloatField()

class Shop_item_table(models.Model):
    shop_id = models.ForeignKey(Shop_table, to_field='id', on_delete=models.CASCADE)
    mainitem_id = models.ForeignKey(Global_item_table, to_field='id', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    remaining = models.IntegerField()
    price = models.FloatField()


class Maintainance_table(models.Model):
    History_id = models.ForeignKey(History_table, to_field='id', on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop_table, to_field='id', on_delete=models.CASCADE)
    item_id = models.ForeignKey(Global_item_table, to_field='id', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user_id = models.ForeignKey(Account_table, to_field='id', on_delete=models.CASCADE)
    is_super = models.BooleanField()

class Qualification(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Request(models.Model):

	qual=(
			(1,"Master Degree"),
			(2,"Bachelor's Degree"),
			(3,"12th Pass"),
			(4,"10th Pass"),
			(5,"Below 10th"),
		)

	name=models.CharField(max_length=40)
	address=models.TextField()
	contact_no=models.CharField(max_length=10)
	email=models.CharField(max_length=30)
	qualification=models.ForeignKey(Qualification,to_field="id",on_delete=models.SET_NULL,null=True)
	region_id=models.ForeignKey(Region_table,to_field="id",on_delete=models.SET_NULL,null=True)
	is_reviewed=models.BooleanField(default=False)


class Monthly_Rating(models.Model):
    history_id = models.ForeignKey(History_table, to_field='id', on_delete=models.CASCADE,default=None)
    rating = models.FloatField(default=0)
    shop_id= models.ForeignKey(Shop_table, to_field='id', on_delete=models.CASCADE,default=None)




