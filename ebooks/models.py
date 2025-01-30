from django.db import models

# Create your models here.
class myBooks(models.Model):

    title=models.CharField(max_length=64)
    author=models.CharField(max_length=64)
    genre=models.CharField(max_length=64)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    stock=models.IntegerField()

    def _str_(self):
        return f"Title: {self.title}, Author:  {self.author},  Genre: {self.genre}, Price: {self.price},Stock:  {self.stock}"