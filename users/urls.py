from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('users', views.CreateUser.as_view(), name='user-create'),
    path('users', views.UpdateUser.as_view(), name='user-update'),
    path('users/<int:pk>', views.ShowUser.as_view(), name='user-detail'),
    path('users/<int:pk>', views.DeleteUser.as_view(), name='user-delete'),
]
