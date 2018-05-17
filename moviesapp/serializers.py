from rest_framework import serializers
from moviesapp.models import Movielist


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movielist
        fields = ('Movie_Id', 'Movie_Name', 'Release_Date', 'Rating')

    def create(self, validated_data):
        """
        Create and return a new `Movielist` instance, given the validated data.
        """
        return Movielist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Movielist` instance, given the validated data.
        """
        instance.Movie_Id = validated_data.get('Movie_Id', instance.Movie_Id)
        instance.Movie_Name = validated_data.get('Movie_Name', instance.Movie_Name)
        instance.Release_Date = validated_data.get('Release_Date', instance.Release_Date)
        instance.Rating = validated_data.get('Rating', instance.Rating)
        instance.save()
        return instance