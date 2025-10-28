from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                        # Homepage
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Details of a single post
    path('create/', views.create_post, name='create_post'),     # Create new post
    path('register/', views.register, name='register'),         # User register
    path('login/', views.login_view, name='login'),             # Login page
    path('logout/', views.logout_view, name='logout'),          # Logout page
]
