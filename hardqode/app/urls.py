from django.urls import path
from .views import *

urlpatterns = [
    path('user/<int:user_id>/lessons/', LessonsList.as_view(), name='lessons'),
    path('user/<int:user_id>/product/<int:product_id>/', ProductLessonsList.as_view(), name='product_lessons'),
    path('statistics/', Statistics.as_view(), name='statistics'),
]
