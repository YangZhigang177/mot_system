from django.urls import path
from . import views

urlpatterns = [
    path('video/<int:id>', views.get_video),

]