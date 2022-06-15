from users.models import CustomUser, Students, Professeur
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class ProfesseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professeur
        fields = '__all__'
        
class UserLoginSerializer(serializers.Serializer):
    user_type_data = ((1, "Admin"), (2, "Professeur"), (3, "Etudiant"))
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    username = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=255)
    user_type = serializers.ChoiceField(choices=user_type_data)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        first_name = data.get("first_name", None)
        last_name = data.get("last_name", None)
        username = data.get("username", None)
        user_type = data.get("user_type", None)
        
        user = authenticate(email=email, password=password, first_name=first_name, last_name=last_name, username=username, user_type=user_type)
        if user is None:
            raise serializers.ValidationError(
                'Un utilisateur avec cet email et ce mot de passe est introuvable !'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError(
                'Utilisateur avec cette Adresse e-mail et le mot de passe indiqués est introuvable !'
            )
        return {
            'email':user.email,
            'username':user.username,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'user_type':user.user_type,
            'token': jwt_token
        }
