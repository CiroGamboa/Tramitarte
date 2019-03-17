from django.urls import path
from webapp import views
# from series import views

urlpatterns = [
    path('home/',views.get_landing,name='getLanding'),
    path('checkCode/<input_code>',views.check_code,name='check_code'),
    path('.well-known/pki-validation/A8299B98AAF2C5FCD66F150704D6B9A2.txt',views.file_down)

]
