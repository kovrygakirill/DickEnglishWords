from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.decorators import action
from django.contrib import auth

from business_logic.loginsys.login import check_valid_user, authorization_user


class LoginViewSet(viewsets.ViewSet):

    def get_page(self, request: Request, *args, **kwargs):
        return render(request, "login.html")

    def authorization(self, request: Request, *args, **kwargs):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        user = authorization_user(username=username, password=password)
        error_valid_user = check_valid_user(user=user)

        if not error_valid_user:
            auth.login(request, user)
            response = redirect("/")
        else:
            args = {"login_error": error_valid_user}
            response = render(request, "login.html", args)

        return response
