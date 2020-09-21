# table/urls.py

from django.urls import path
from django.views.generic import TemplateView

from table.views import(
    tableDataAPI, addItemTable,
    updateItemTable, deleteItemTable)


app_name = 'table'
urlpatterns = [
    path('', TemplateView.as_view(
        extra_context={'title': 'home'},
        template_name='index.html'), name='home'),
    path('table/api/', tableDataAPI, name='api'),
    path('table/add/', addItemTable, name='add'),
    path('table/update/', updateItemTable, name='update'),
    path('table/delete/', deleteItemTable, name='delete')
]
