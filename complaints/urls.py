from django.urls import path
from complaints import views
from .views import ContactSubmissionView, DocumentUploadView, QueryView

urlpatterns = [
    path('', views.who_are_you_reporting, name='submit_complaint'),
    path('newspaper_form/', views.newspaper_form, name='newspaper_form'),
    path('bank_form/', views.bank_form, name='bank_form'),
    path('solicitor_form/', views.solicitor_form, name='solicitor_form'),
    path('barrister_form/', views.barrister_form, name='barrister_form'),
    path('judge_form/', views.jcio_form, name='judge_form'),
    path('download_form/<str:file_path>', views.download_form, name='download_form'),
    path('success/', views.success_page, name='success_page'),
    path('contact/', ContactSubmissionView.as_view(), name='contact-api'),
    path('documents/', DocumentUploadView.as_view(), name='document-upload'),
    path('query/', QueryView.as_view(), name='query'),
]


