from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.decorators import action
from django.contrib import auth

from business_logic.loginsys.login import authorization_user
from business_logic.loginsys.validator import Validator
from business_logic.loginsys.register import create_not_active_user

import logging

logger = logging.getLogger(__name__)


class LoginViewSet(viewsets.ViewSet):
    validator = Validator()

    def get_page(self, request: Request):
        return render(request, "login.html")

    def authorization(self, request: Request):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        user = authorization_user(username=username, password=password)
        error_valid_user = self.validator.get_error_valid_user(user=user)

        if not error_valid_user:
            auth.login(request, user)
            response = redirect("/")
            logger.info(f"Authorization of User({username})")
        else:
            args = {"login_error": error_valid_user}
            response = render(request, "login.html", args)
            logger.info(f"User({username}) wasn't authorization")

        return response


class RegisterViewSet(viewsets.ViewSet):
    validator = Validator()

    def get_page(self, request: Request):
        return redirect('login')

    def registration(self, request: Request):
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        c_password = request.POST.get("confirm_password", "")

        error_valid_fields = self.validator.get_error_valid_fields(username=username, email=email)

        if not error_valid_fields:
            not_active_user = create_not_active_user(username=username, email=email, password=password)
            # send_email_for_register(email, user_profile.user.id)
            response = render(request, "login.html")
        else:
            args = {"register_error": error_valid_fields}
            response = render(request, "login.html", args)
            logger.info(f"Registration crushed for User({username}) with Email({email})")

        return response
