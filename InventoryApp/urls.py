from django.urls import path
from .views import *

urlpatterns = [
    path('products/add', ProdViews.as_view()),
    path('products/', ProdViews.as_view()),  
    path('products/<int:id>', ProdViewsbyID.as_view()),
    path('category/', categoryview.as_view()),
    path('category/add', categoryview.as_view()),
    path('category/<int:id>', catViewsByID.as_view()),
]
