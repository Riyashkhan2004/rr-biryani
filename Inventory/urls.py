from django.urls import path
from . import views


urlpatterns = [

    # Login
    path(
        'login/',
        views.user_login,
        name='login'
    ),


    # Home
    path("", views.home, name="index"),


    # About
    path(
        'about/',
        views.about,
        name='about'
    ),


    # Services
    path(
        'services/',
        views.services,
        name='services'
    ),


    # Menu
    path(
        'menu/',
        views.menu,
        name='menu'
    ),


    # Food Order Page
    path(
        'order/<int:id>/',
        views.order_page,
        name='order_page'
    ),


    # Simple Order Page
    path(
        'order/',
        views.order,
        name='order'
    ),


    # Contact
    path(
        'contact/',
        views.contact,
        name='contact'
    ),


    # Add To Cart
    path(
        'add-to-cart/<int:id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),


    # Admin Order Page
    path(
        'admin-order/',
        views.admin_order,
        name='admin_order'
    ),
    path('food/edit/<int:id>/', views.edit_food, name='edit_food'),
path('food/delete/<int:id>/', views.delete_food, name='delete_food'),

]