from rest_framework import serializers

from hotel.models import Hotel, RoomCategory, Room, Booking


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('name',)


class RoomCategorySerializer(serializers.ModelSerializer):
    hotel = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Hotel.objects.all())

    class Meta:
        model = RoomCategory
        fields = ('name', 'hotel', 'min_price',)


class RoomSerializer(serializers.ModelSerializer):
    room_category = serializers.SlugRelatedField(many=False, slug_field='name', queryset=RoomCategory.objects.all())

    class Meta:
        model = Room
        fields = ('name', 'room_category',)


class BookingSerializer(serializers.ModelSerializer):
    room = serializers.SlugRelatedField(many=False, slug_field='id', queryset=Room.objects.all(), write_only=True)
    room_name = serializers.CharField(source='room.name', read_only=True)

    class Meta:
        model = Booking
        fields = ('room', 'room_name', 'date_check_in', 'date_check_out',)
        read_only_fields = ('room_name',)
        write_only_fields = ('room',)
