from django.contrib import admin

from hotel.models import Hotel, RoomCategory, Room, Booking

admin.site.register(Hotel)
admin.site.register(RoomCategory)
admin.site.register(Room)
admin.site.register(Booking)
