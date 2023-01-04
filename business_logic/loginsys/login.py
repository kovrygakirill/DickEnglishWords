from django.contrib import auth
from django.contrib.auth.models import User


def authorization_user(username: str, password: str) -> User | None:
    return auth.authenticate(username=username, password=password)


def check_valid_user(user: User | None) -> str:
    error = ''

    if user is None:
        error = "User wasn't found"
    elif not user.user_profile.is_confirm:
        error = "Confirm registration(The letter sent to email)"

    return error
