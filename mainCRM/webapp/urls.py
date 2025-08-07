from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.userLogin, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.userLogout, name='logout'),
    path('create-record/', views.createRecord, name='createrecord'),
    path('view/<int:record_id>/', views.viewRecord, name='view_record'),
    path('update/<int:record_id>/', views.updateRecord, name='update_record'),
    path('delete/<int:record_id>/', views.deleteRecord, name='delete_record'),
    path('search/', views.searchRecord, name='search_record'),
]