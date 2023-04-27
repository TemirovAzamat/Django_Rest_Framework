from django.urls import path

from .views import doctor_list_create_api_view, PatientListCreateAPIView

urlpatterns = [
    path('doctors/', doctor_list_create_api_view),
    path('patients/', PatientListCreateAPIView.as_view()),
]