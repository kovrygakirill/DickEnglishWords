from django.urls import path, re_path
from .views import LoginViewSet, RegisterViewSet


login = LoginViewSet.as_view({
    'get': 'get_page',
    'post': 'authorization'
})
register = RegisterViewSet.as_view({
    'get': 'get_page',
    'post': 'registration'
})

urlpatterns = [
    path(r'login/', login, name='login'),
    path(r'register/', register, name='register'),
]

