from django.contrib.auth.models import User
from django.db import transaction
from django.db import DatabaseError

from apps.loginsys.models import UserProfile
from business_logic.my_exceptions import ProblemWithDataBase
import logging

logger = logging.getLogger(__name__)


def create_user_profile(username: str, email: str, password: str) -> UserProfile:
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
    except DatabaseError as de:
        logger.error(f"User({username}) wasn't created!!! {repr(de)}")
        raise ProblemWithDataBase("User wasn't created, because Database have problems!")

    return user_profile
