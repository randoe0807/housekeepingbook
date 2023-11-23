from django.urls import path, includ
from django.contrib import admin

app_name = 'housekeepingbook'

urlpatterns = [
    path('admin/', admin.site.urls),
]