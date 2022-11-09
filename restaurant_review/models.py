from datetime import date, datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20)
    rating=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.CharField(max_length=500)
    review_date = models.DateTimeField('review date')    
    def __str__(self):
        return self.restaurant.name + " (" + self.review_date.strftime("%x") +")"

class Profile(models.Model):        
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experiment_one = models.BooleanField(default=False) #is experiment one complete
    experiment_one_result = models.BooleanField(default=True) #true = yes false = no
    experiment_one_retake_count = models.IntegerField(default=0) #number of retakes 
     
    experiment_two = models.BooleanField(default=False) #is experiment two complete
    experiment_two_day = models.IntegerField(default=0) #day cnt of photo taken
    experiment_two_last_photo_date = models.DateField(default=date(1999, 1, 1)) #date of last photo taken
    experiment_two_selection = models.CharField(default='', max_length=10)
    experiment_two_edited = models.CharField(default='', max_length=10)
    experiment_two_num_edited_selected = models.IntegerField(default=0)

    experiment_two_retake_count_1 = models.IntegerField(default=0) #number of retakes on day 1
    experiment_two_retake_count_2 = models.IntegerField(default=0) #number of retakes on day 2
    experiment_two_retake_count_3 = models.IntegerField(default=0) #number of retakes on day 3
    experiment_two_retake_count_4 = models.IntegerField(default=0) #number of retakes on day 4
    experiment_two_retake_count_5 = models.IntegerField(default=0) #number of retakes on day 5
    experiment_two_retake_count_6 = models.IntegerField(default=0) #number of retakes on day 6

    isARCamera = models.BooleanField(default=True) #show participant AR camera
    showARImage = models.BooleanField(default=True) #show participant AR image 
    tellIsAR = models.BooleanField(default=False) #tell participant camera is AR 

    hasConsent = models.BooleanField(default=False) #participant has filled in consent form
    survey_one_isComplete = models.BooleanField(default=False) #participant has filled in survey one
    survey_two_isComplete = models.BooleanField(default=False) #participant has filled in survey two 
    hasLottery = models.BooleanField(default=False) #participant has signed up for lottery 


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @property
    def isPhotoTaken(self):
        return date.today() == self.experiment_two_last_photo_date
 
    # @property 
    # def isComplete(self):
    #     return self.experiment_two_day >= 7
    