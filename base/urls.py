from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('news/',news,name='news'),
    path('blogs/',blogs,name='blogs'),
    path('sports/',sports,name='sports'),
    path('international/',international,name='international'),
    path('about/',about,name='about'),
    path('read/<int:pk>',read,name='read'),
    path('read1/<int:pk>',read1,name='read1'),
    path('read2<int:pk>',read2,name='read2'),
    path('read3<int:pk>',read3,name='read3'),
    path('read4/<int:pk>',read4,name='read4'),
    path('read5/<int:pk>',read5,name='read5'),

]