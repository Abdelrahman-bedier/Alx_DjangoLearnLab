from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books

urlpatterns = [
    path('books/', views.list_books, name='books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.SignUpView.as_view(), name='register')
]