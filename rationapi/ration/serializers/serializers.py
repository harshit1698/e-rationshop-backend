import datetime

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from ration.models import *

# getting user model
User = get_user_model()


class Qualification_Serializer(ModelSerializer):
    class Meta:
        model=Qualification
        fields='__all__'




class Region_Serializer(ModelSerializer):
    class Meta:
        model=Region_table
        fields='__all__'



class Request_Create_Serializer(ModelSerializer):
    region_id=Region_Serializer()
    qualification=Qualification_Serializer()
    class Meta:
        model=Request
        fields='__all__'

class Request_Create1_Serializer(ModelSerializer):
    # region_id=Region_Serializer()
    # qualification=Qualification_Serializer()
    class Meta:
        model=Request
        fields='__all__'


class Global_item_Serializer(ModelSerializer):
    class Meta:
        model = Global_item_table
        fields = '__all__'

class Region_Serializer(ModelSerializer):
    class Meta:
        model=Region_table
        fields = '__all__'

class AccountSerializer(ModelSerializer):
    class Meta:
        model=Account_table
        fields = '__all__'



class Request_Serializer(ModelSerializer):
    shopkeeper_id=AccountSerializer()
    region_id=Region_Serializer()
    class Meta:
        model= Shop_table
        fields = ['id','shopkeeper_id','region_id','address','contact_no']

################################## UserRegisterSerializer ##########################################

# this serializer will match 2 passwords and confirms them and also create the user object
class UserRegisterSerializer(ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'},write_only=True)
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields= [
            'first_name',
            'last_name',
            # 'username',
            'email',
            'password',
            'password2',

        ]
        extra_kwargs = {'password':{'write_only':True}}

    def validate(self, attrs):
        pw=attrs.get('password')
        pw2 = attrs.pop('password2')
        if pw != pw2:
            raise serializers.ValidationError("Password must match")
        return attrs

    def create(self, validated_data):
        print(validated_data)
        user_obj = User(
            username=validated_data.get('email'),
            email = validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name = validated_data.get('last_name')
        )
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        return user_obj

class Year_Serializer(ModelSerializer):
    class Meta:
        model=History_table
        fields=['year']







