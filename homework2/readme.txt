Readme.txt

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

add ID # to url ie: /Movies/(id here) for update, delete and read
book seats:
http://127.0.0.1:8000/api/Bookings/
booking history:
