import datetime

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

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data['date_check_in'] < datetime.date.today():
            raise serializers.ValidationError("You can book only starting from tomorrow")

        if data['date_check_in'] > data['date_check_out']:
            raise serializers.ValidationError("Check out must occur after check in")

        filter_params = dict(date_check_in=data['date_check_in'],
                             date_check_out=data['date_check_out'])
        is_occupied = Booking.objects.filter(**filter_params, room=data['room']).exists()

        if is_occupied:
            raise serializers.ValidationError(
                "Room had already been booked for for this date. Please, choose another one.")

        return data
