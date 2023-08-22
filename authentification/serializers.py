from rest_framework import serializers

from .models import UserProfile


class UserInscriptionSerializer(serializers.ModelSerializer):
    # register serializer
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, label='Confirm password')

    class Meta:
        model = UserProfile
        fields = ['id',
                  'username',
                  'password',
                  'password2',
                  'first_name',
                  'last_name',
                  'email',
                  'can_be_contacted',
                  'can_data_be_shared',
                  'age', ]
        read_only_fields = ['id']

    # at least 15 years old to agree share the datas
    def validate_age(self, value):
        if value < 15 and self.initial_data.get('can_data_be_shared'):
            raise serializers.ValidationError('You are too young to share datas.')
        return value

    # validate password and confirm password is the same
    def validate(self, attrs):
        password1 = attrs.get('password')
        password2 = attrs.get('password2')
        if password2 != password1:
            raise serializers.ValidationError({'password2': 'You must enter the same password.'})
        attrs.pop('password2')
        return attrs

    # re write the create method to encrypt the password
    def create(self, validated_data):
        password = validated_data['password']
        user = self.Meta.model(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id',
                  'username',
                  'first_name',
                  'last_name',
                  'email', ]
        read_only_fields = ['id']

    # def update(self, instance, validated_data):
    #     password = validated_data['password']
    #     if password:
    #         instance.set_password(password)
    #     return super().update(instance, validated_data)
