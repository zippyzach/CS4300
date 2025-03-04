#Zachary Donnelly - CS4300 HW2

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from datetime import date, timedelta
from rest_framework.test import APIClient
from rest_framework import status

#tests that movie is created properly and all parts of the model are populated as expected through assertations
#tests model and API endpoints
class MovieTest(TestCase):
    
    def test_create(self):
        
        movie = Movie.objects.create(title="Test Movie", description="a test movie",date=date(2020,2,2), duration=timedelta(hours=2,minutes=2))
        
        self.assertEqual(movie.title, "Test Movie")
        self.assertEqual(movie.description, "a test movie")
        self.assertEqual(movie.date, date(2020,2,2))
        self.assertEqual(movie.duration, timedelta(hours=2,minutes=2))

class MovieAPITest(TestCase):
        def setUp(self):
            self.user = User.objects.create_user(username='test user', password='test_password')
            self.client = APIClient()
            self.movie = Movie.objects.create(title="Test Movie", description="a test movie",date=date(2020,2,2), duration=timedelta(hours=2,minutes=2))
        
        def test_create(self):
            url = '/api/Movies/'
            data = {
            'title': 'Test Movie',
            'description': 'a test movie',
            'date': '2020-2-2',
            'duration': '02:02:00',
            }
            
            response = self.client.post(url, data,format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
 
#tests that seat is created properly and all parts of the model are populated as expected through assertations
#tests model and API endpoints     
class SeatTest(TestCase):
    
    def test_create(self):
        movie = Movie.objects.create(title="Test Movie", description="a test movie",date=date(2020,2,2), duration=timedelta(hours=2,minutes=2))
    
        seat = Seat.objects.create(movie=movie,number="A1",booked_status=False)
        
        self.assertEqual(seat.movie.title, "Test Movie")
        self.assertEqual(seat.number, "A1")
        self.assertFalse(seat.booked_status)
            
class SeatAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test user', password='test_password')
        self.client = APIClient()
        self.movie = Movie.objects.create(title="Test Movie", description="a test movie",date=date(2020,2,2), duration=timedelta(hours=2,minutes=2))
        
        
        
    def test_create(self):
        url = '/api/Seats/'
        data = {
            'movie': self.movie.id,
            'number': 'A1',
            'booked_status': False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
#tests that booking is created properly and all parts of the model are populated as expected through assertations
#tests model and API endpoints
class BookingTest(TestCase):
    
    def test_create(self):
         user = User.objects.create_user(username='test_user_1', password='test_password')
         movie = Movie.objects.create(title="Test Movie", description="a test movie",date=date(2020,2,2), duration=timedelta(hours=2,minutes=2))
         
         seat = Seat.objects.create(movie=movie,number="A1",booked_status=False)
         booking = Booking.objects.create(movie_title=movie, seat=seat, user=user)
         
         self.assertEqual(booking.movie_title.title, "Test Movie")
         self.assertEqual(booking.seat.number, "A1")
         self.assertEqual(booking.user.username, "test_user_1")

class BookingAPITest(TestCase):
        def setUp(self):
            self.user = User.objects.create_user(username='test user', password='test_password')
            self.client = APIClient()
            self.movie = Movie.objects.create(title="Test Movie", description="a test movie",date=date(2020,2,2), duration=timedelta(hours=2,minutes=2))
            
            self.seat = Seat.objects.create(movie=self.movie, number = "A1",booked_status=False)
            
        def test_create(self):
            url = '/api/Bookings/'
            data = {
                'movie_title': self.movie.id,
                'seat': self.seat.id,
                'user': self.user.id
            }
            
            response = self.client.post(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)