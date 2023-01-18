from django.contrib import auth
from django.contrib.auth.models import User


def authorization_user(username: str, password: str) -> User | None:
    return auth.authenticate(username=username, password=password)
