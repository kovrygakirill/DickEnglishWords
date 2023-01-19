from django.contrib.auth.models import User
from django.db import transaction
from django.db import DatabaseError

from loginsys.models import UserProfile
import logging

logger = logging.getLogger(__name__)


def create_not_active_user(username: str, email: str, password: str) -> UserProfile | None:
    try:
        with transaction.atomic():
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            user.save()

            user_profile = UserProfile.objects.create(user=user)
            user_profile.save()

        logger.info(f"User({username}) was created")
    except DatabaseError:
        user_profile = None
        logger.error(f"Error's in DataBase, User({username}) wasn't created!!!")

    return user_profile
