from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('delete/<int:pid>', views.delete, name='delete'),
    path('update/<int:uid>', views.update, name='update')
]
