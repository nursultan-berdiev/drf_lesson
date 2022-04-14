from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    popularity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name
