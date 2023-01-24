from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from .views import Login
app_name = 'items'

urlpatterns = [
    path('',views.index,name='index'),
    path('post/<str:param>/',views.write,name='write'),
    path('topicwrite/',views.topicwrite,name='topicwrite'),
    path('login/',views.account_login,name='login'),
    path('create/',views.sign,name='create'),
    path('logout/',views.out,name='logout'),
    path('search/',views.search,name='search'),
    path('searchpost/<str:param>/',views.searchpost,name='searchpost')
]