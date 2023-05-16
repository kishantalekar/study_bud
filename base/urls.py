from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings
urlpatterns =[
    path('',views.home,name='home'),
    path('room/<str:pk>',views.room,name='room'),
    path('create-room/',views.createroom,name='create-room'),
    path('update-room/<str:pk>',views.updateroom,name='update-room'),
    path('delete-room/<str:pk>',views.deleteroom, name='delete-room'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('register/',views.registeruser,name='register'),
    path('delete-message/<str:pk>',views.deletemessage,name='delete-message'),
    path('profile/<str:pk>',views.userProfile,name='user-profile'),
    path('update-user',views.updateUser,name='update-user'),
    path('topics/',views.topicsPage,name='topics'),
    path('activity/',views.activityPage,name='activity')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)