from django.db import models
from django.urls import reverse
from users.models import User


class Category(models.Model):

    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.CharField(max_length=100, db_index=True, unique=True)
    image1 = models.ImageField(upload_to='product', blank=True)
    image2 = models.ImageField(upload_to='product', blank=True)
    image3 = models.ImageField(upload_to='product', blank=True)
    image4 = models.ImageField(upload_to='product', blank=True)
    image5 = models.ImageField(upload_to='product', blank=True)
    image6 = models.ImageField(upload_to='product', blank=True)
    image7 = models.ImageField(upload_to='product', blank=True)
    image8 = models.ImageField(upload_to='product', blank=True)
    image9 = models.ImageField(upload_to='product', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    uploaded = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product', args=[self.slug])

class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum([basket.sum() for basket in self])

    def total_quantity(self):
        return sum([basket.quantity for basket in self])


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Card for {self.user.username} | Product: {self.product.name} | Quantity {self.quantity}'

    def sum(self):
        return self.product.price * self.quantity
    
