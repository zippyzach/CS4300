Zachary Donnelly - CS4300 HW2
Readme.txt

to Run:
while in directory containing manage.py
py manage.py runserver

go to url http://127.0.0.1:8000/movie_list/
from here click a movie to view seats, book seats and view booking history


relevant files:
serializers.py - holds the relevant serializers for setting up the RESTful APIs
urls.py - holds the urls for the project and the router for the APIs
models.py - holds the models for Movie, Seat, and Bookings
views.py - holds the views for the API as well as the visual representation of Movie, Seat, and Bookings
signals.py - holds the signal to create 20 seats when a movie is created.
apps.py - controls the signal to create 20 seats when a movie is created.
settings.py - controls the middleware, installed apps and database settings.
base.html - holds the base html for all other html files to inherit - for the purpose of this project it stores the buttons to traverse the app
movie_list.html - holds the list of movies
seat_booking.html - holds the seats for a given movie and allows them to be reserved
booking_history.html - holds booking history for a current user
tests.py - holds the tests for models and API endpoints

to run tests - 6 in all, 3 for html views and 3 for api endpoints
py manage.py test

A default test user is automatically logged in for testing purposes named "test user" due to timing constraints on implementing a full authentication ability.
If this user is not set up here are the steps:
py manage.py shell
from django.contrib.auth.models import User
test_user = User.objects.create_user(username='test user', password='password123')
test_user.save()
exit()

A default movie will also be needed with ID 1
if this is not in the database here are the steps:
py manage.py shell
from booking.models import Movie
from datetime import timedelta
movie = Movie.objects.create(title="Sample Movie", description="A sample movie", date="2025-03-01", duration=timedelta(120))
movie.save()
exit()

APIs can be accessed for movies, book seats, and check booking history - CRUD functionality through REST framework is available

add movies:
http://127.0.0.1:8000/api/Movies/

add ID # to url ie: /Movies/(id here)/ for update, delete and read
book seats:
http://127.0.0.1:8000/api/Bookings/
booking history:
http://127.0.0.1:8000/api/Bookings/