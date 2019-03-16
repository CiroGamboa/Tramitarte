from django.urls import path
from webapp import views
# from series import views

urlpatterns = [
    path('home/',views.get_landing,name='getLanding'),
    path('checkCode/<input_code>',views.check_code,name='check_code')

]
