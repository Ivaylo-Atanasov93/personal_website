from django.urls import path

from .views import ContactMe

urlpatterns = [
    path('', ContactMe.as_view(), name='contact'),
]
