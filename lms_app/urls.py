from django.urls import path
from . import views
from .views import BookListView

urlpatterns=[
   path('',views.index,name='index'), 
   path('books/', BookListView.as_view(), name='books'), 
   path('update/<int:id>',views.update,name='update'),
   path('delete/<int:id>',views.delete,name='delete'),




]