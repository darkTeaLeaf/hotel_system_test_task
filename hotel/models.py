from django.contrib.auth.models import User
from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=100, help_text='Name of a hotel')

    def __str__(self):
        return self.name


class RoomCategory(models.Model):
    hotel = models.ManyToManyField(Hotel, help_text='A hotel where the category presents')
    name = models.CharField(max_length=100, help_text='Name of a category')
    min_price = models.DecimalField(max_digits=12, decimal_places=2, help_text='Minimal price for room in a category')

    def __str__(self):
        return self.name

    def get_hotel(self):
        return self.hotel


class Room(models.Model):
    room_category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE, help_text='Category of a room')
    name = models.CharField(max_length=100, help_text='Name of a room')

    def __str__(self):
        return self.name

    def get_hotel(self):
        return self.room_category.hotel


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, help_text='Booked room')
    date_check_in = models.DateField(help_text='Check in date')
    date_check_out = models.DateField(help_text='Check out date')

    def __str__(self):
        return self.room.name + str(self.date_check_in)

    def get_hotel(self):
        return self.room.room_category.hotel
