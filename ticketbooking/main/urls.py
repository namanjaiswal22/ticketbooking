from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('eventregister',views.eventregister,name="eventregister"),
    path('showallevent',views.showallevent,name="showallevent"),
    path('showoneevent/<str:id>',views.showoneevent,name="showoneevent"),
    path('deleteevent/<str:id>',views.deleteevent,name="showoneevent"),
    path('login',views.login,name="login"),
    path('register',views.register,name='register'),
    path('logout',views.logout,name="logout"),
    path('book/<str:id>',views.book,name="book"),
    path('bookedevent',views.bookedevent,name="bookedevent"),
    path('createdevent',views.createdevent,name="createdevent")
]
