from django.urls import path
from .views import *
urlpatterns = [
    path('',homeview,name = 'home'),
    path('add', add, name = 'add'),
    path('edit', update_view,name = 'update_view' ),
    path('update/<int:pk>', update, name = 'update'),
    path('/delete/<int:pk>/', delete_view, name="delete-function"),
]
