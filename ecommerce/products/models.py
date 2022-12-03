from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse

from .utils import unique_slug_generator
# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=100)
    slug        = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price       = models.DecimalField(max_digits=10, decimal_places=2,)
    image       = models.ImageField(upload_to='photos/%Y/%m/%d/%M/%S', null=True, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('products-detail', kwargs={'slug' : self.slug })

    def __str__(self):
        return self.title
    


def product_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_reciever, sender=Product)