from rest_framework import serializers
from tempSignin.models import tempUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = tempUser
        fields = ["id", "name", "Uuid", "email", "expiration"]
