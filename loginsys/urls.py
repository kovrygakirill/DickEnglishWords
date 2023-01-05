from django.urls import path, re_path
from .views import LoginViewSet


login = LoginViewSet.as_view({
    'get': 'get_page',
    'post': 'authorization'
})

urlpatterns = [
    path(r'login/', login, name='login'),
]

