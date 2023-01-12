from django.db import models

# Create your models here.
class Our_dogs (models.Model):
    dog_name = models.CharField (max_length=30)
    dog_age = models.IntegerField ()
    dog_history = models.CharField (max_length=500)
    dog_status = models.BooleanField(default=True)
    image = models.ImageField (upload_to = 'Our dogs' )

class Our_volunteers (models.Model):
    volunteer_name = models.CharField (max_length=30)
    volunteer_age = models.IntegerField ()
    volunteer_reason_to_be_a_volunteer = models.CharField(max_length=500)
    volunteer_favourite_dog_and_reason = models.CharField(max_length=500)
    image = models.ImageField (upload_to = 'Our volunteers' )

class Our_collaborative_institutions (models.Model):
    instituion_name = models.CharField (max_length=30)
    institution_reason_to_colaborate = models.CharField (max_length =500)
    institution_vision_of_animals = models.CharField (max_length=500)
    image = models.ImageField (upload_to = 'Our collaborative institutions' )

class Others_projects (models.Model):
    project_name = models.CharField(max_length=30)
    institution_or_person_in_charge = models.CharField (max_length=30)
    project_objective =models.CharField (max_length =500)
    image = models.ImageField (upload_to = 'Others projects' )
