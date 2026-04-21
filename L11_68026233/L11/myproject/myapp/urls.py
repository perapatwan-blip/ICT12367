from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_person),   # เข้าเว็บ = หน้า สมัคร
    path('list', views.index),    # หน้า ตาราง
]