from django.urls import path
from botapp import views

urlpatterns = [
    path('receiveCode/<input_code>',views.receive_code,name='receive_code')
    
]
