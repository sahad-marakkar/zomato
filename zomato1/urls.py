from django.urls import path
from .import views

urlpatterns=[
    path('home',views.index,name='sahad'),
    path('index',views.home,name='fahim'),
    path('sahad',views.sahad,name='rasal'),
    path('guppy',views.boot,name='text'),
    path('',views.boot,name='text'),
    path('java',views.javascript,name='text'),
    path('joom',views.conditions,name='ss'),
    path('jaaa',views.boot2,name='sos'),
    path('www',views.try1,name='web'),
    path('abc',views.dome,name='stone'),  
    path('abcd',views.dom1,name='ston'),       
    path('calcu',views.calc,name='stonm'), 

]
