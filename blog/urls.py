from django.urls import path

from . import views


app_name= "blog"

urlpatterns = [
    path('', views.index, name='list'),
    path('<int:blog_id>', views.show, name='detail')
]