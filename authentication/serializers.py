from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Serializer extends TokenObtainPairSerializer by adding is_doctor to payload."""

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_doctor'] = user.profile.is_doctor
        return token
