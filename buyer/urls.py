from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name='buyer-home'),
    path('how_it_works/', views.how_it_works, name='buyer-how it works'),
    path('my_purchases/', views.my_purchases, name='buyer-my purchases'),
    path('popular_products/', views.popular_products, name='buyer-popular products'),
    path('my_profile', views.my_profile, name='buyer-my profile'),
    
]