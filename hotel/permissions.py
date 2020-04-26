from rest_framework import permissions


class IsHotelRelated(permissions.BasePermission):
    """
    Object-level permission to only allow only hotel related users to view it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.get_hotel() == request.user.hotel
