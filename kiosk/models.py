from django.db import models

class Category(models.Model):
    category_name = models.CharField('BEVERAGE_TYPE',max_length=20)

    def __str__(self):
        return self.category_name
    
class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=40, unique=True)
    price = models.IntegerField(default='0')

    def __str__(self):
        return self.menu_name
    
class Customer(models.Model):
    customer_name = models.CharField(max_length=100)

class Order(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
