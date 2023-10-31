from django.db import models

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(blank=True)
    ordered_date = models.DateTimeField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Call(models.Model):

    title = models.CharField(max_length=70)
    phonenb = models.IntegerField()
    des = models.TextField(blank=True)
    dpt = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return str(self.title)

