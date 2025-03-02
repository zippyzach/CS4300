
from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    
    #movie title
    title = models.CharField(max_length=200)
    #description of the movie
    description = models.TextField()
    #release date of the movie
    date = models.DateField()
    #run time of the movie
    duration = models.DurationField()
    
    def __str__(self):
        return self.title
        

class Seat(models.Model):

    #using char field to allow for sections and number sequences
    number = model.CharField(max_length=5)
    #bool to check if booked or not, not booked(false) by default
    status = models.booleanField(default = False)


    def __str__(self):
        return self.number
      

class Booking(models.Model):
    
    #the movie title for the booking request
    #all foreign keys delete any booking if the movie, seat, or user are deleted
    movie_title = models.ForeignKey(Movie,on_delete=models.CASCADE)
    #the seat requested in the booking
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    #the user who requested the booking
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #the date the booking was requested
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f" Booking information for movie: {self.movie_title.title} seat #: {self.seat.number} for user: {self.user.username}"

