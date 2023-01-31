from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    is_confirm = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')

    class Meta:
        db_table = "user_profile"

    def __str__(self):
        return str(self.user)
