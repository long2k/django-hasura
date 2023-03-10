from django.contrib import admin
from django.urls import path, include, re_path
from products.views import ProductViewset
from rest_framework import routers
from accessory.settings import ADMIN_URL

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Accessory Shop API",
      default_version='v1',
      description="Accessory Shop API",
   ),
   public=True,
)

router = routers.DefaultRouter()
routing_viewsets = [ProductViewset]

for r in routing_viewsets:
    if hasattr(r, "endpoint_url"):
        router.register(r.endpoint_url, r, basename= r.endpoint_url)
    else:
        q =  r.serializer_class.Meta.model
        router.register(r"%s.%s" % (q._meta.app_label, q.__meta__.lower()), r)

urlpatterns = [
     re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(f'{ADMIN_URL}', admin.site.urls),
    path('api/', include(router.urls))
]
