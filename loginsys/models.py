from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    is_confirm = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')

    class Meta:
        db_table = "user_profile"

    def __str__(self):
        return str(self.user)


class TokenEmail(models.Model):
    key = models.CharField(max_length=20)
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='token_email')

    class Meta:
        db_table = "token_email"

    def __str__(self):
        return self.key
