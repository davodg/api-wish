"""wishlist_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from core.views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Wish List API",
        default_version='v1',
        description="An api for wishlists",
        contact=openapi.Contact(email="davidgb061@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'', WishViewSet, basename='wishviewset')

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/wish/', include('core.urls')),
    path('wishes/', include(router.urls)),
    path('random/', RandomView.as_view(), name='random'),
    path('<pk>/update', FulfilledView.as_view(), name='update_post'),
    path('api/auth/', include('authentication.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
