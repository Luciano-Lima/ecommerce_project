from django.urls import path, include
from .views import home, logout, login, register, profile
# from users import url_reset

urlpatterns = [
    path('logout/', logout, name="logout"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('profile/', profile, name="profile"),
    # path('password-reset/', include(url_reset))
]