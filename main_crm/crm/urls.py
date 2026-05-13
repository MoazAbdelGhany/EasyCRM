from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index , name = 'index' ),
    #Auth
    path('register/', views.register , name = 'register' ),
    path('login/', views.login_view , name = 'login'),
    path('dashboard/', views.dashboard , name = 'dashboard'),
    path('logout/', views.logout_view , name = 'logout'),

    #Records
    path('create_record/', views.create_record , name = 'create_record'),
    path('view_record/<int:record_id>/', views.view_record , name = 'view_record'),
    path('update_record/<int:record_id>/', views.update_record , name = 'update_record'),
    path('delete_record/<int:record_id>/', views.delete_record , name = 'delete_record'),
    path('search_records/', views.search_records , name = 'search_records'),

    #Categories
    path('create_category/', views.create_category , name = 'create_category'),
    path('update_category/<int:category_id>/', views.update_category , name = 'update_category'),
    path('delete_category/<int:category_id>/', views.delete_category , name = 'delete_category'),
    path('search_category/', views.search_category , name='search_category')

]
   