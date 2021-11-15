from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('delete/<int:id>/', views.deleteView, name = 'deleteView'),
    path('bill-form/', views.formView, name = 'formView'),
    path('pdf/<int:id>/', views.pdf, name='pdf'),
]