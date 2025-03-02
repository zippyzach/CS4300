#Zachary Donnelly - CS4300 HW2
from rest_framework import serializers
from .models import Movie, Seat, Booking

#movie serializer
class M_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
 
#seat serializer
class S_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

#booking serializer
class B_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
    