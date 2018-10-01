from datetime import datetime
from django.core.validators import MinValueValidator
from django.db import models

class Order(models.Model):
    """ Order with customer details """
    address = models.CharField(
        'Street Address', null=True, blank=True, max_length=500)
    email = models.EmailField('Email', null=False, blank=False)
    name = models.CharField('Name', max_length=250)
    order_date = models.DateTimeField('Order Date', default=datetime.now)
    phone = models.CharField('Phone', null=True, blank=True, max_length=250)

    def __str__(self):
        return 'Order {0}'.format(self.id)


class Product(models.Model):
    """ Collection of products """
    description = models.CharField('Description', max_length=500)
    name = models.CharField('Name', max_length=250)
    in_stock = models.IntegerField('Quantity In Stock', default=1)
    picture = models.ImageField(
        'Picture', upload_to='products/%Y/%m/%d/', null=True, blank=True)
    picture_thumbnail = models.ImageField(
        'Thumbnail Picture', upload_to='products/thumbnails/%Y/%m/%d/', null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return '{0} - ${1} ({2} in stock)'.format(self.name, self.price, self.in_stock)


class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(
        default=0, validators=[MinValueValidator(1)])

    def __str__(self):
        return 'Order {0}: {1}'.format(self.order.id, self.product.name)
