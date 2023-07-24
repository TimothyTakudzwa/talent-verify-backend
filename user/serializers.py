from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'company', 'is_staff')

    def create(self, validated_data):
        # Extract the password from the validated data
        password = validated_data.pop('password', None)

        # Create a new user instance with other validated data
        user = self.Meta.model(**validated_data)

        if password is not None:
            # Use the create_user method to set the password securely
            user.set_password(password)

        # Save the user instance to the database
        user.save()
        return user