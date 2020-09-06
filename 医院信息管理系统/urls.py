
from django.contrib import admin
from django.urls import path
from hospital import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('c/', views.adsf, name='a'),
    path('del/', views.Del_data.as_view(), name='del'),
    # path('change/', views.ChangeData.as_view(), name='change'),
    path('change/', views.change, name='change'),
    path('login/', views.Login.as_view(), name='login'),
    path('adduser/', views.AddUser.as_view(), name='adduser')
]
