#Zachary Donnelly - CS4300 HW2

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from datetime import date, timedelta

#tests that movie is created properly and all parts of the model are populated as expected through assertations
class MovieTest(TestCase):
    
    def test_create(self):
        
        movie = Movie.objects.create(title="Test Movie", description="a test movie",date=date(2020,2,2), duration=timedelta(hours=2,minutes=2))
        
        self.assertEqual(movie.title, "Test Movie")
        self.assertEqual(movie.description, "a test movie")
        self.assertEqual(movie.date, date(2020,2,2))
        self.assertEqual(movie.duration, timedelta(hours=2,minutes=2))
        
#tests that seat is created properly and all parts of the model are populated as expected through assertations       
class SeatTest(TestCase):
    
    def test_create(self):
        movie = Movie.objects.create(title="Test Movie", description="a test movie",date=date(2020,2,2), duration=timedelta(hours=2,minutes=2))
    
        seat = Seat.objects.create(movie=movie,number="A1",booked_status=False)
        
        self.assertEqual(seat.movie.title, "Test Movie")
        self.assertEqual(seat.number, "A1")
        self.assertFalse(seat.booked_status)
    
#tests that booking is created properly and all parts of the model are populated as expected through assertations
class BookingTest(TestCase):
    
    def test_create(self):
         user = User.objects.create_user(username='test_user_1', password='test_password')
         movie = Movie.objects.create(title="Test Movie", description="a test movie",date=date(2020,2,2), duration=timedelta(hours=2,minutes=2))
         
         seat = Seat.objects.create(movie=movie,number="A1",booked_status=False)
         booking = Booking.objects.create(movie_title=movie, seat=seat, user=user)
         
         self.assertEqual(booking.movie_title.title, "Test Movie")
         self.assertEqual(booking.seat.number, "A1")
         self.assertEqual(booking.user.username, "test_user_1")