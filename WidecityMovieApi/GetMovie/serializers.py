from rest_framework import serializers
class movie_serializer(serializers.Serializer):
    class Meta:
        fields = '__all__'