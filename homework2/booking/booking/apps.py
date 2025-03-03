#Zachary Donnelly - CS4300 HW2

from django.apps import AppConfig

class BookingConfig(AppConfig):
    name = 'booking'
    
    def ready(self):
        import booking.signals