from rest_framework import routers

from hotel.views import HotelViewSet, RoomCategoryViewSet, RoomViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'room_categories', RoomCategoryViewSet, basename='RoomCategory')
router.register(r'rooms', RoomViewSet, basename='Room')
router.register(r'room_categories/(?P<category_id>\d+)/rooms', RoomViewSet,
                basename='RoomCategory')
router.register(r'bookings', BookingViewSet, basename='Booking')
router.register(r'rooms/(?P<room_id>\d+)/bookings', BookingViewSet, basename='Room')

urlpatterns = router.urls
