
from django.urls import path

from nsfw_detection import views


urlpatterns = [
    path('',views.home,name='home' ),
    path('imagefile',views.imagefile,name='imagefile'),
    
]   