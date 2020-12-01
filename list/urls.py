
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('about/', views.about, name='about'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('cross_off/<int:pk>', views.cross_off, name='cross_off'),
    path('uncross/<int:pk>', views.uncross, name='uncross'),
    path('edit/<int:pk>', views.edit, name='edit'),
]