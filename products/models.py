from django.db import models
from django.urls import reverse
from accounts.models import User
import uuid


# Create your models here.
class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:category_filter', args=[self.slug, ])


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='products/',
                              default="products/default.jpg")
    description = models.TextField()
    price = models.FloatField(default=0, null=True, blank=True)
    count_in_stock = models.IntegerField(default=0, null=True, blank=True)
    available = models.BooleanField(default=False)
    discount = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('products:product-detail', args=[self.id, ])

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def get_product_price(self):
        if self.discount > 0:
            discounted_price = (self.discount / 100) * self.price
            return self.price - discounted_price
        return self.price

