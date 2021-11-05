from django.db import models
from django.utils import timezone

# ! Variable global 
global image_diractory
image_diractory = "child_app/Storage"

# Create your models here.
class Parent(models.Model):
    FirstName = models.CharField(verbose_name="Parent first Name",blank=False , max_length=30)
    LastName = models.CharField(verbose_name="Parent Last Name",blank=False , max_length=30)
    DOB = models.DateField(default=timezone.now)
    Image = models.ImageField(upload_to=image_diractory, height_field=500, width_field=500, max_length=None)

class Place(models.Model):
    name = models.CharField(verbose_name="Place Name",blank=False , max_length=30)
    longitude = models.DecimalField(max_digits=5, decimal_places=2 ,blank=False)
    attiude = models.DecimalField(max_digits=5, decimal_places=2 , blank=False)


class Enfant(models.Model):
    EducationChoices = (
        ('P1', '1 ére primaire'),
        ('P2', '2 éme primaire'),
        ('P3', '3 éme primaire'),
        ('P4', '4 éme primaire'),
        ('P5', '5 éme primaire'),
        ('P6', '6 éme primaire'),
        ('S1', '7 éme secondaire'),
        ('S2', '8 éme secondaire'),
        ('S3', '9 éme secondaire'),
        ('L1', '1 ére lycée'),
        ('L2', '2 éme lycée'),
        ('L3', '3 éme lycée'),
        ('L4', '4 éme lycée'),
    )
    FirstName = models.CharField(verbose_name="Child Last Name",blank=False , max_length=30 )
    LastName = models.CharField(verbose_name="Child Last Name",blank=False , max_length=30)
    DOB = models.DateField(default=timezone.now)
    Education = models.CharField(choices=EducationChoices , blank=True , null= True , max_length= 14)
    Image = models.ImageField(upload_to=image_diractory, height_field=500, width_field=500, max_length=None)

    id_parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    id_place = models.ManyToManyField(Place)

class Emplacement(models.Model):
    SiteName = models.CharField(max_length=50)
    SiteAdresse = models.CharField(max_length=50)
    Remark = models.CharField(max_length=50)



class Tache(models.Model):
     Task_Status = (
        ('F', 'Finished'),
        ('P', 'In Progress'),
        ('N', 'Not Started'),
    )
     TaskName = models.CharField(verbose_name="Task name ", max_length=50)
     Duration = models.DurationField()
     StartDate = models.DateField(auto_now=False, auto_now_add=False)
     EndDate = models.DateField(auto_now=False, auto_now_add=False)
     TaskStatus = models.CharField(max_length=1 , choices=Task_Status)
     TaskType = models.CharField(max_length=10)

     child_id = models.ForeignKey(Enfant, on_delete=models.CASCADE)
     Emplacement_id =models.ForeignKey(Emplacement, on_delete=models.CASCADE)



class Rapport(models.Model):
    RapportDate = models.DateField(default=timezone.now)
    TextDate = models.CharField(max_length=50)
    Problems = models.CharField(blank=True , max_length=50)

    id_Tache = models.OneToOneField(Tache, on_delete=models.CASCADE)






class Message(models.Model):
    Contenu = models.CharField(blank=False , max_length=256)
    Date = models.DateField()
    id_enfant=models.ForeignKey(Enfant,on_delete=models.CASCADE)