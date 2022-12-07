from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('post',views.post_home,name='post_home'),
    path('about',views.about,name='about'),
    path('create',views.about,name='create'),
    path('create_post',views.create_post,name='create_post')

]