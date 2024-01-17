from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('statuses/', StatusListCreate.as_view(), name='statuses_list_create'),
    path('persons/', PersonsListCreate.as_view(), name='persons_list_create'),
]
