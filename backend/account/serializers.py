from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from .models import User

class CustomRegisterSerializer(RegisterSerializer):
    email =  serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    nickname = ser4ializers.CharField(required=True)
    
    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'email': self.validated_data.get('email'),
            'password': self.validated_data.get('password'),
            'nickname': self.validated_data.get('nickname'),
        }
        
class CustomUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'nickname')
        read_only_fields = ('email', )
