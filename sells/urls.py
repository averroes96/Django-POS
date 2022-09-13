from sells.views import ClientsViewSet

from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clients', ClientsViewSet, basename="clients")

urlpatterns = [
    path("", include(router.urls))
]