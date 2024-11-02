from . import views
from django.urls import path

urlpatterns = [
    path('products/', views.product_list),

    path('products/<int:pk>/', views.product_detail),

    path('collections/',views.get_collection,name='collection'),

    path('collection/<int:pk>/',views.collection_detail,name='collection')
]
