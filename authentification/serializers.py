from django.contrib.auth.models import User
from rest_framework import serializers

from .models import UserProfile


class UserInscriptionSerializer(serializers.ModelSerializer):
    # register serializer
    username = serializers.CharField(max_length=15
                                      )

    class Meta:
        model = UserProfile
        fields = ['username',
                  'password',
                  'can_be_contacted',
                  'can_data_be_shared',
                  'age']

    # def validate_age(self,value):
    #     if int(value) < 15 :