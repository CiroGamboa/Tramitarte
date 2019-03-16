from django.urls import path
from webapp import views
# from series import views

urlpatterns = [
#     path('series/', views.serie_list),
#     path('series/(?P<pk>[0-9]+)/', views.serie_detail),
    path('webapp/home',views.getLanding),
    path('webapp/checkCode',views.check_code)
]
