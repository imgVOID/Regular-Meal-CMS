from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class DeliveryVendor(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    price_one_delivery = models.DecimalField(default=0.0, max_digits=12, decimal_places=2)


@receiver(pre_save, sender=DeliveryVendor)
def delivery_vendor_pre_save(sender, instance, **kwargs):
    print('DeliveryVendor created.')


class DeliverySchedule(models.Model):
    delivery_vendor = models.ForeignKey(DeliveryVendor, on_delete=models.CASCADE, null=True)
    delivery_time = models.DurationField()


@receiver(pre_save, sender=DeliverySchedule)
def delivery_vendor_pre_save(sender, instance, **kwargs):
    print('DeliverySchedule created.')

