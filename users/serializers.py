from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from datetime import datetime, timedelta    
from .models import User
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','password' ,'first_name','last_name',
                   'phone_number', 'role', 'address', 'profile_picture']
        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'read_only': True},
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},

        }

    def create(self, validated_data):
       user = User.objects.create_user(**validated_data)
       return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()
        return instance
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    #override default field to use email instead of username
    #means users can login with email instead of username
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #remove the default username field
        self.fields.pop('username', None)
        #add email field
        self.fields['email'] = serializers.EmailField(required=True)
        self.fields['password'] = serializers.CharField(write_only=True, required=True)

    @classmethod
    def get_token(cls, user):
        return super().get_token(user)
    
    def validate(self, attrs):
        #extract email and password from request
        email = attrs.get('email')
        password = attrs.get('password')

        if not email or not password:   
            raise serializers.ValidationError("Email and password are required")
        
        #check for email and password
        user = User.objects.filter(email=email).first()
        if user and user.check_password(password):
            self.user = user
        else:
            raise serializers.ValidationError("Invalid email or password")
        
        #Generate token
        data = {}
        refresh_token = self.get_token(user)
        data['refresh'] = str(refresh_token)
        data['access'] = str(refresh_token.access_token)
        data['user'] = UserSerializer(user).data
        return data    
