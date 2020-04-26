from rest_framework import mixins, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from hotel.models import Hotel, RoomCategory, Room, Booking
from hotel.permissions import IsHotelRelated
from hotel.serializers import HotelSerializer, RoomCategorySerializer, RoomSerializer, BookingSerializer


class HotelViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericViewSet):
    """
        retrieve:
        Return the hotel specified by id.

        list:
        Return a list of all the existing hotels.

    """
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class RoomCategoryViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          GenericViewSet):
    """
        retrieve:
        Return the room category specified by id.

        list:
        Return a list of all the existing room categories.

    """
    serializer_class = RoomCategorySerializer
    permissions_classes = [IsAuthenticated, IsHotelRelated]

    def get_queryset(self):
        return RoomCategory.objects.filter(hotel=self.request.user.profile.hotel)


class RoomViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  GenericViewSet):
    """
        retrieve:
        Return the room specified by id.

        list:
        Return a list of all the existing rooms. If room category is specified, the list is filtered by it.

    """
    serializer_class = RoomSerializer
    permissions_classes = [IsAuthenticated, IsHotelRelated]

    def get_queryset(self):
        if 'category_id' in self.kwargs:
            return Room.objects.filter(room_category_id=self.kwargs['category_id'])

        return Room.objects.filter(room_category__in=RoomCategory.objects.filter(hotel=self.request.user.profile.hotel))


class BookingViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     GenericViewSet):
    """
        retrieve:
        Return the booking specified by id.

        list:
        Return a list of all the existing bookings. If room is specified, the list is filtered by it.

    """
    serializer_class = BookingSerializer
    permissions_classes = [IsAuthenticated, IsHotelRelated]

    def get_queryset(self):
        if 'room_id' in self.kwargs:
            return Booking.objects.filter(room_id=self.kwargs['room_id'])

        return Booking.objects.filter(room__in=Room.objects.filter(
            room_category__in=RoomCategory.objects.filter(hotel=self.request.user.profile.hotel)))

