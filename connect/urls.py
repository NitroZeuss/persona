from .views import MessageViewSet
from rest_framework.routers import SimpleRouter
from django.urls import path

# router = SimpleRouter()
# router.register(r'message/', MessageViewSet)
# router.urls


# urlpatterns = router.urls

urlpatterns = [
    path('message/', MessageViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('message/<int:pk>/', MessageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]