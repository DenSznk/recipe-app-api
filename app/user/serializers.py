"""
Serializers for the users API view
"""
from django.contrib.auth import get_user_model

from rest_framewokr import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user objects"""

    class Meta:
        mode = get_user_model()
        fields = [
            'email',
            'password',
            'name'
            ]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_lenghts': 5,
                }
        }

    def create(self, validated_data):
        """Create and return a user with encrypted password"""

        return get_user_model().objects.crete_user(**validated_data)
