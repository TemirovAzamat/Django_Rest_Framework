from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from Project import settings

schema_view = get_schema_view(
   openapi.Info(
      title="Hospital Api",
      default_version='alpha-0.0.1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="azamatt04@mail.ru"),
      license=openapi.License(name="No license"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

swagger_urlpatterns = [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=6000))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('App.urls')),
] + swagger_urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
