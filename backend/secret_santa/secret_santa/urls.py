"""
URL configuration for secret_santa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings

urlpatterns = [
    # Root path for the API
    path('', include(('participant.urls', 'participants'))),
    path('', include(('draw.urls', 'draws'))),
    # Path to set the API documentation 
    path('APIDocu', SpectacularSwaggerView.as_view(url_name='participants'), name='swagger-ui'),
    # Path to downlaod the API swagger file 
    path('APIDocu/schema', SpectacularAPIView.as_view(), name='participants'),
    # Path to the admin page
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
