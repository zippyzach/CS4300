#Zachary Donnelly - CS4300 HW2
#this will signal to create 20 seats when a movie is created


from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Movie, Seat

@receiver(post_save, sender=Movie)
def create_seats(sender, instance, created, **kwargs):
        if created:
            for i in range(1, 21):
                seat_number = f"S{i}"
                Seat.objects.create(movie=instance, number=seat_number)
