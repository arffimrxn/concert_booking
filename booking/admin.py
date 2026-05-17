from django.contrib import admin
from .models import Concert, Booking, AuditLog

admin.site.register(Concert)
admin.site.register(Booking)
admin.site.register(AuditLog) 