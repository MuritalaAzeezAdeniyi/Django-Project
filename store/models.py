from django.db import models
from django.conf import settings

# Create your models here.

class Collection(models.Model):
    title = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveSmallIntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collections = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotion = models.ManyToManyField('Promotions',related_name='+')

    def __str__(self):
        return f'{self.title} {self.price} '




class Cart(models.Model):
    create_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    PAYMENT_STATUS = [
        ('P','PENDING'),
        ('S','Success'),
        ('F','Failed')
    ]

    placement = models.DateTimeField(auto_now_add=True)
    payment_statue = models.CharField(max_length=1,choices= PAYMENT_STATUS,default='p')
    customer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)



class CartItem(models.Model):
       cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
       product = models.ForeignKey(Product,on_delete=models.CASCADE)
       quantity = models.PositiveSmallIntegerField()


class OrderItem(models.Model):

      order = models.ForeignKey(Order,on_delete=models.PROTECT)
      product = models.ForeignKey(Product,on_delete=models.CASCADE)
      quantity = models.PositiveSmallIntegerField()
      unit_price = models.DecimalField(max_digits=6,decimal_places=2)


class Promotions(models.Model):
      product = models.ManyToManyField(Product, related_name='+')
      discount = models.DecimalField(max_digits=6,decimal_places=2)


class Address(models.Model):
      numbers = models.PositiveSmallIntegerField()
      street = models.CharField(max_length=255)
      state = models.CharField(max_length=255)
      country = models.CharField(max_length=255)
      customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



      def __str__(self):
          return f"{self.numbers} {self.title} {self.state} {self.country}"


