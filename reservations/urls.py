from .api import ReservationViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('api/reservations', ReservationViewSet, 'reservations')

urlpatterns = router.urls