from rest_framework import routers

from hotel.views import HotelViewSet, RoomCategoryViewSet, RoomViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'hotels/(?P<hotel_id>\d+)/room_categories', RoomCategoryViewSet, basename='Hotel')
router.register(r'hotels/(?P<hotel_id>\d+)/rooms', RoomViewSet, basename='Hotel')
router.register(r'hotels/(?P<hotel_id>\d+)/room_categories/(?P<category_id>\d+)/rooms', RoomViewSet,
                basename='RoomCategory')
router.register(r'hotels/(?P<hotel_id>\d+)/bookings', BookingViewSet, basename='Hotel')
router.register(r'hotels/(?P<hotel_id>\d+)/rooms/(?P<room_id>\d+)/bookings', BookingViewSet, basename='Room')

urlpatterns = router.urls
