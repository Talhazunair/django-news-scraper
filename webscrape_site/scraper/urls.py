from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('search',views.search_content,name='search'),
    path('login',views.login_user,name='login'),
    path('signup',views.signup_user,name='signup'),
    path('content',views.show_content,name='content'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.logout_user,name='logout'),
    path('download_csv',views.export_csv,name='download_csv'),
]