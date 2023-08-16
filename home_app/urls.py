from django.urls import path
from home_app.views import index_view

urlpatterns = [
    path('',index_view,name='index')
]