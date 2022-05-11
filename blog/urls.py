from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('addblog/', views.addBlog, name='addblog'),
    path('<int:id>/', views.updateBlog, name='updateblog'),
    path('delete/<int:id>/', views.deleteBlog, name='deleteblog')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
