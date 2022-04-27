from django.urls import path, include

from .views import index_view

from allauth.account.views import LoginView

appname = "datacleaner"

urlpatterns = [
    path("service/", index_view, name='index'),
    path("", LoginView.as_view(), name="account_login"),
    path('accounts/', include('allauth.urls')),
]