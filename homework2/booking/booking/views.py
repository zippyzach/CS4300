#Zachary Donnelly - CS4300 HW2

from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import M_Serializer, S_Serializer, B_Serializer
from django.shortcuts import render, get_object_or_404


#view sets for API
#movie view set
class M_View_Set(viewsets.ModelViewSet):
    
    queryset = Movie.objects.all()
    serializer_class = M_Serializer

#seat view set
class S_View_Set(viewsets.ModelViewSet):
    
    queryset = Seat.objects.all()
    serializer_class = S_Serializer
    

#booking view set
class B_View_Set(viewsets.ModelViewSet):
    
    queryset = Booking.objects.all()
    serializer_class = B_Serializer
    
#html view

def movie_list(request):
    m_list = Movie.objects.all()
    
    return render(request, 'booking/movie_list.html', {'movies': m_list})
    
def seat_booking(request):
    movie = get_object_or_404(Movie, id=movie_id)
    s_list = Seat.objects.all()
    
    return render(request, 'booking/seat_booking.html', {'movie': movie, 'seats': s_list})

def booking_history(request):
    
    b_list = Booking.objects.filter(user=request.user)
    
    return render(request, 'booking/booking_history.html', {'bookings': b_list})