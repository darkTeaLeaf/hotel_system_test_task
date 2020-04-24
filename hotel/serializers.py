from django.contrib.auth.models import User
from rest_framework import serializers

from hotel.models import Hotel, Profile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, help_text='Required. Password must contain at least 8 characters')
    hotel = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Hotel.objects.all(),
                                         source='profile.hotel')

    class Meta:
        model = User
        fields = (
            'id', 'username', 'password', 'email', 'first_name', 'last_name', 'hotel')
        write_only_fields = ('password',)
        extra_kwargs = {
            'email': {
                'help_text': 'Email address of a user'
            },
            'first_name': {
                'help_text': 'Name of a user'
            },
            'last_name': {
                'help_text': 'Surname of a user'
            }
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])

        profile_data = validated_data.get('profile')

        if profile_data:
            profile = Profile.objects.create(user=user, hotel=profile_data['hotel'])
            profile.save()
            user.profile = profile
            user.save()

        return user

    def update(self, instance, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])

        profile_data = validated_data.get('profile')

        if profile_data:
            user.profile.hotel = profile_data['hotel']
            user.save()

        return instance


class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
