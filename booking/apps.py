from django.apps import AppConfig

class BookingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'

    # This 'ready' function tells Django to turn on our signals when the server starts
    def ready(self):
        import booking.signals