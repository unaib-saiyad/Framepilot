from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'mobile_number', 'date_of_birth', 'password']
        extra_kwargs = {'mobile_number': {'required': True}}

    username = serializers.CharField(
        max_length=10,
        style={'input_type': 'text', 'placeholder': 'Name'},
    )
    email = serializers.EmailField(
        max_length=100,
        style={'input_type': 'email', 'placeholder': 'Email', 'required': 'required'},
    )
    mobile_number = serializers.IntegerField(
        style={'input_type': 'number', 'placeholder': 'Mobile number'}
    )
    date_of_birth = serializers.DateTimeField(
        style={'input_type': 'date', 'placeholder': 'Date of birth'}
    )
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'},
        required=True
    )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    username = serializers.CharField(
        max_length=10,
        style={'input_type': 'text', 'placeholder': 'Name'},
    )
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'},
        required=True
    )

