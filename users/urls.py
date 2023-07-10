from django.urls import path, include
from .views import logout, login, register, profile

from users import url_reset

urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('register/', register, name="register"),
    path('profile/', profile, name="profile"),
    path('password_reset/', include(url_reset))
]
