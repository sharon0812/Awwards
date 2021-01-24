from django.urls import path
from . import views
from . views import PostDetailView, PostCreateView, index
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [
    path('',index, name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('search/', views.search_results, name='search_results'),
    
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)