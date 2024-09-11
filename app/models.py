from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__ (self):
        return self.name


class Book(models.Model):
    #value to be displayed and enother for db
    book_status =[
        ('available', 'available'),
        ('borrowed', 'borrowed'),
        ('sold', 'sold')
    ]
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    ISBN = models.IntegerField()
    publication_year = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null = True, blank = True)
    status = models.CharField(max_length=50, choices = book_status, null = True, blank = True)
    category = models.ForeignKey(Category, on_delete=PROTECT)

    def __str__(self):
        return self.name

