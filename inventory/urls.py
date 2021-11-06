from django.urls import path
from . import views

urlpatterns = [
    path('index/inventory/', views.IndexView, name='IndexView'),
    path('index/inventory/add_item/', views.add_itemform, name='add_itemform'),
    path('index/inventory/add_item/import_structure', views.import_structure_download, name='import_structure_download'),
    path('index/inventory/all_units/', views.all_units, name='all_units'),


]