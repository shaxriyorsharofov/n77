from django.urls import path
from .views import *

urlpatterns = [
    path('', CategoryCreate.as_view(), name='category-create')
]
