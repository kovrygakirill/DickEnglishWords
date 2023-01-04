from django.shortcuts import render, redirect
from django.contrib import auth
from business_logic.loginsys.login import check_valid_user, authorization_user


def login(request):
    if request.POST:
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
    else:
        response = render(request, "login.html")

    return response
