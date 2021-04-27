from django.urls import path
from . import views
from django.conf.urls import include, url
from .views import dashboard, register

urlpatterns = [
    path("", views.finalapp_index, name="finalapp_index"),
    path("<int:pk>/", views.finalapp_detail, name="finalapp_detail"),
    path("<category>/", views.finalapp_category, name="finalapp_category"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^register/", register, name="register"),
    url(r"^oauth/", include("social_django.urls")),
]



