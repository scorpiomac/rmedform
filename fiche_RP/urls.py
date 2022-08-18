from django.urls import path
from . import  views
urlpatterns=[
    path('',views.information,name='information'),
    path('add/',views.multistepformexample,name='add'),

    path('test/',views.createpost,name='test')
]