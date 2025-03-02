#Zachary Donnelly - CS4300 HW2
from rest_framework import serializers
from .models import Movie, Seat, Booking

class M_serializer(serializers.ModleSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
 
 
 class S_Serializer(serializers.ModleSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

class B_Serializer(serializers.ModleSerializer):
    class Meta:
        model = Booking
        fields = '__all__'