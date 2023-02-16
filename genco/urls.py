from django.urls import path
from . import views 

urlpatterns=[
    path('',views.index, name='index'),
    path('/generated',views.generated, name='generated')
]