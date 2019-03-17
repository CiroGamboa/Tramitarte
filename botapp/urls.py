from django.urls import path
from botapp import views

urlpatterns = [
    path('receiveCode/<input_code>',views.receive_code,name='receive_code'),
    path('',views.doc_view,name='doc_view'),
    path('sendDoc/',views.receive_doc,name='receive_doc')
    
]
