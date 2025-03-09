from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("download/", views.download_result, name="download"),
    path("api/translit/", views.translit_api, name="translit_api"),
    path('features/', views.features, name='features'),
    path('contact/', views.contact, name='contact'),
]

