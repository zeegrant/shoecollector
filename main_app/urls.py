from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shoes/', views.shoes_index, name='index'),
    path('shoes/<int:shoe_id>/', views.shoes_detail, name='detail'),
    path('shoes/create/', views.ShoeCreate.as_view(), name='shoes_create'),
    path('shoes/<int:pk>/update/', views.ShoeUpdate.as_view(), name='shoes_update'),
    path('shoes/<int:pk>/delete/', views.ShoeDelete.as_view(), name='shoes_delete'),
    path('shoes/<int:shoe_id>/add_storage/', views.add_storage, name='add_storage'),
    path('socks/', views.SockList.as_view(), name='socks_index'),
    path('socks/<int:pk>/', views.SockDetail.as_view(), name='socks_detail'),
    path('socks/create/', views.SockCreate.as_view(), name='socks_create'),
    path('socks/<int:pk>/update/', views.SockUpdate.as_view(), name='socks_update'),
    path('socks/<int:pk>/delete/', views.SockDelete.as_view(), name='socks_delete'),
    path('shoes/<int:shoe_id>/assoc_sock/<int:sock_id>/', views.assoc_sock, name='assoc_sock'),
]
