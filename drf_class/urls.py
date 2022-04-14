from unicodedata import category

from django.contrib import admin
from django.urls import path, include
from store import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category', views.CategoryAPIView, basename='category')
router.register('book', views.BookAPIViewSet, basename='Book')

urlpatterns = [
    path('admin/', admin.site.urls),



    # path('', views.CategoryAPIView.as_view({
    #     'get': 'list',
    #     'post': 'create',
    # })),
    # path('<int:pk>/', views.CategoryAPIView.as_view({
    #         'get': 'retrieve',
    #         'put': 'update',
    #         'delete': 'destroy',
    #     })),

    path('', include(router.urls))


    # path('<int:pk>/', views.CategoryRetrieveAPIView.as_view()),
    # path('<int:pk>/delete/', views.CategoryDestroyAPIView.as_view()),
    # path('<int:pk>/update/', views.CategoryUpdateAPIView.as_view()),
]
