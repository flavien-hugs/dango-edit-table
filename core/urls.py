"""core URL Configuration
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('table.urls', namespace='table')),
    path('admin/', admin.site.urls),
]
