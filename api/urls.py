from django.urls import path
from . import views

urlpatterns = [
    path('',views.uploadpage,name='api'),
    path('view',views.show,name='view'),
    path('updateapi',views.apioverview,name='updateapi'),
    path('upload',views.upload,name='upload'),
    path('table',views.table,name='table'),
    path('getdata',views.getdata,name='getdata')


]