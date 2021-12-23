from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('sale/',views.sale,name='sale'),
    path('contact/',views.contacts,name='contacts'),
    path('register/',views.register,name='register'),
     path('login/',views.userlogin,name='login'),
     path('logout/',views.userlogout,name='logout'),
     path('services/<int:pk>',views.zapis,name='zapis'),
     path('person/<int:pk>',views.person,name='person'),
     path('order/<int:pk>',views.order,name='order'),
]