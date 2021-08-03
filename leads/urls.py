from django.urls import path
# from django.contrib import admin
# from django.conf import settings
# from django.conf.urls.static import static

from .views import (
   LeadListView, LeadDetailView , LeadCreateView, LeadUpdateView, UploadView,
   LeadDeleteView, CategoryListView, CategoryDetailView, LeadCategoryUpdateView , BooklistView  ,UploadbookView
)

app_name = "leads"

urlpatterns = [
     path('', LeadListView.as_view(), name = 'lead-list'),
     path('<int:pk>/', LeadDetailView.as_view(), name = 'lead-detail'),
     path('create/', LeadCreateView.as_view(), name = 'lead-create'),
     path('<int:pk>/update/', LeadUpdateView.as_view(), name = 'lead-update'),
     path('<int:pk>/delete/', LeadDeleteView.as_view(), name = 'lead-delete'),

     # class based
     path('upload/', UploadView.as_view(), name = 'lead-upload'),
    # path('upload/', DocumentListView.as_view(), name = 'lead-upload'),
      
      # function based
     path('books/',BooklistView , name = 'lead-books'),
     path('books/documents', UploadbookView, name = 'lead-upload'),

     
     path('categories/', CategoryListView.as_view(), name = 'category-list'),
     path('categories/<int:pk>/', CategoryDetailView.as_view(), name = 'category-detail'),
     path('categories/<int:pk>/category', LeadCategoryUpdateView.as_view(), name = 'lead-category-update'),

]

