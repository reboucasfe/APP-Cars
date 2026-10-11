from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    print('## POST DELETE ##')
    print(instance)
    cars_count = Car.objects.all().count()
cars_value = Car.objects.aggregate(
    total_value=sum('value')
)['total_value']
CarInventory.objects.create(
    cars_count=cars_count,
    cars_value=cars_value
    )

