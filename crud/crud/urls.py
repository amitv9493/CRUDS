
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from functioncrud.views import delete_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('function/',include('functioncrud.urls')),
    path('classcrud/',include('classcrud.urls')),
    # path('delete/<int:pk>/', delete_view, name = 'delete-function'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
