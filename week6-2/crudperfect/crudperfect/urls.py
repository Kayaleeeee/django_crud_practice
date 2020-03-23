"""crudperfect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from perfect import views

# New img
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('detail/<int:post_pk>/', views.detail, name='detail'),
    path('edit/<int:post_pk>/', views.edit, name='edit'),
    path('delete/<int:post_pk>/', views.delete, name='delete'),
    path('detail/<int:post_pk>/<int:comment_pk>',
         views.delete_comment, name='delete_comment'),

    # 댓글은 경로도 같이 삭제해야 하는데, 경로 찾기는 디테일에서!

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
