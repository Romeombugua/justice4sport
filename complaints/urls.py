from django.urls import path
from complaints import views

urlpatterns = [
    path('', views.submit_complaint, name='submit_complaint'),
]
