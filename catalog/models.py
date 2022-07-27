from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="images/")

    class Meta:
        app_label = "catalog"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(default=0)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        app_label = "catalog"

    def __str__(self):
        return self.name

        
