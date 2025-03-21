from django.urls import path
from . import views


urlpatterns = [
    # Bus views
    path('', views.bus_list, name='bus_list'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register_view, name='register_view'),
    path('buses/<int:pk>/', views.bus_detail, name='bus_detail'),

    # Schedule views
    path('schedules/', views.schedule_list, name='schedule_list'),

    # Booking views
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/new/', views.booking_create, name='booking_create'),
    path('bookings/<int:pk>/delete/', views.booking_delete, name='booking_delete'),
    path('bookings/new/<int:bus_id>/<int:seat_number>/', views.booking_create, name='booking_create'),
]
