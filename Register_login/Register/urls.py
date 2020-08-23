from django.urls import path, include
from Register import views
app_name = 'Register'

urlpatterns = [
            path('registration', views.registration, name='registration'),
            path('logging_in', views.logging_in, name='logging_in'),
            
]
