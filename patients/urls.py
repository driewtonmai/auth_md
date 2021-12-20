from django.urls import path

from .views import LastPatientsListAPIView

urlpatterns = [
    path('lasts/', LastPatientsListAPIView.as_view(), name='last_patients_list'),
]
