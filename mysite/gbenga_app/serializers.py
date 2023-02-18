from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'last_name', 'first_name',
                  'linked_in_profile', 'twitter_profile',
                  'github_profile', 'about_me')
