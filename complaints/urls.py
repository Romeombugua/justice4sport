from django.urls import path
from complaints import views

urlpatterns = [
    path('', views.submit_complaint, name='submit_complaint'),
    path('download_form/<str:file_path>', views.download_form, name='download_form'),
]
