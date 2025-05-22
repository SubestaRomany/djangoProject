from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    book_list_create,              
    BookUpdateAPIView,              
    BookGenericDetailView,         
    BookViewSet                     
)

# Router for ViewSet
router = DefaultRouter()
router.register('books-viewset', BookViewSet, basename='book')

urlpatterns = [
    path('books/', book_list_create, name='book-list-create'),                         
    path('books/update/<int:pk>/', BookUpdateAPIView.as_view(), name='book-update'),   
    path('books/detail/<int:pk>/', BookGenericDetailView.as_view(), name='book-detail'),
    path('', include(router.urls)),                                                    
]
