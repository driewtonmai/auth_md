from django.urls import path

from .views import LastPatientsListAPIView


app_name = 'patients'

urlpatterns = [
    path('lasts/', LastPatientsListAPIView.as_view(), name='last_patients_list'),
]
