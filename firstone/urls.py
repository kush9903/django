from django.urls import path
from . import views
urlpatterns = [
    path('',views.myfunccall,name='index'),
    path('about',views.about,name='about'),
    path('add/<int:a>/<int:b>',views.add,name='add'),
    path('name/<str:name1>/<int:age>',views.name,name='name'),
    path('firstpage',views.firstpage,name='firstpage'),
    path('secondpage',views.secondpage,name='secondpage'),
    path('thirdpage',views.thirdpage,name='thirdpage'),
    path('fourthpage',views.fourthpage,name='fourthpage'),
    path('fifthpage',views.fifthpage ,name='fifthhpage'),
    path('upload',views.upload,name='upload')

]