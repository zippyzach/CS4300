#Zachary Donnelly - CS4300 HW2

from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import M_Serializer, S_Serializer, B_Serializer

#movie view set
class M_View_Set(viewsets.ModelViewSet):
    
    queryset = Movie.objects.all()
    serializer_class = M_Serializer

#seat view set
class S_View_Set(viewsets.ModelViewSet):
    
    queryset = Seat.ojects.all()
    serializer_class = S_Serializer
    

#booking view set
class B_View_Set(viewsets.ModelViewSet):
    
    queryset = Booking.objects.all()
    serializer_class = B_serializer