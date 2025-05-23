"""
URL configuration for jal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Schema View Configuration
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="API for project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

    


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include("user.urls")),
    path('api/',include("bill_invoice.urls")),
    path('api/Billinvoice_item/',include('Billinvoice_Items.urls')),
    path('api/stock/',include('item.urls')),
    path('api/supplier/',include('supplier.urls')),
    path('api/staff/',include('staff.urls')),
    path('api/report/',include('report.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('openapi/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]

   
