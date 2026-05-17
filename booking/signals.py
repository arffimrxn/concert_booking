from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.dispatch import receiver
from .models import AuditLog

# This tripwire triggers when a login is successful
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    AuditLog.objects.create(
        user=user,
        action=f"Successful login by {user.username}"
    )

# This tripwire triggers when someone types the wrong password or username
@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    # Safely get the username they tried to use (no passwords logged!)
    attempted_username = credentials.get('username', 'Unknown')
    AuditLog.objects.create(
        action=f"Failed login attempt for username: '{attempted_username}'"
    )