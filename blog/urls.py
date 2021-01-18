from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('diary/', views.PostDiaryView.as_view(), name='blog-diary'),
    path('portfolio/', views.PostPortfolioView.as_view(), name='blog-portfolio'),
    # path('portfolio/blender/', views.PostBlenderView.as_view(), name='portfolio-blender'),
    # path('portfolio/pm/', views.PostPMView.as_view(), name='portfolio-pm'),
    path('contact/', views.PostContactView.as_view(), name='blog-contact'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
