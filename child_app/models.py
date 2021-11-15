from django.db import models
from django.utils import timezone

# ! Variable global 
global image_diractory
image_diractory = "child_app/Storage"

# Create your models here.

# ! Abstract class for person

class Person(models.Model):

    FirstName = models.CharField(verbose_name="Person First Name",blank=False , max_length=30)
    LastName  = models.CharField(verbose_name="Person Last Name",blank=False , max_length=30)
    DOB       = models.DateField(default=timezone.now)
    Image     = models.ImageField(upload_to=image_diractory, height_field=500, width_field=500, max_length=None)


    class Meta:
        # abstract = True : cette class ne sera pas traduit en une table au niveau de base de donnée.
        # abstract = True : elle va étre utiliser que dans les relations d'héritage.
        abstract = True
        verbose_name = "Person"
        verbose_name_plural = "Persons"




class Parent(Person):

    class Meta:
        db_table = "Parent"
        verbose_name = "Parent"
        verbose_name_plural = "Parents"



class Place(models.Model):
    name      = models.CharField(verbose_name="Place Name",blank=False , max_length=30)
    longitude = models.DecimalField( max_digits = 5 , decimal_places = 2 , blank = False)
    attiude   = models.DecimalField( max_digits = 5 , decimal_places = 2 , blank = False)

    class Meta:
        db_table = "Place"
        verbose_name = "Place"
        verbose_name_plural = "Place"



class Emplacement(models.Model):
    SiteName = models.CharField(max_length=50)
    SiteAdresse = models.CharField(max_length=50)
    Remark = models.CharField(max_length=50)

    class Meta:
        db_table = "Emplacement"
        verbose_name = "Emplacement"
        verbose_name_plural = "Emplacements"



class Enfant(Person):

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

    Education = models.CharField(choices=EducationChoices , blank=True , null= True , max_length= 14)

    id_parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    id_place = models.ManyToManyField(Place)
    
    class Meta:
        db_table = "Enfant"
        verbose_name = "Enfant"
        verbose_name_plural = "Enfants"



class Tache(models.Model):
     Task_Status = (
        ('F', 'Finished'),
        ('P', 'In Progress'),
        ('N', 'Not Started'),
    )
    
     TaskName   = models.CharField(verbose_name="Task name", max_length=50)
     TaskStatus = models.CharField(max_length=1 , choices=Task_Status)
     TaskType   = models.CharField(max_length=10)
     Duration   = models.DurationField()
     StartDate  = models.DateField(default=timezone.now , auto_now=False, auto_now_add=False)
     EndDate    = models.DateField(default=timezone.now , auto_now=False, auto_now_add=False)

     child_id = models.ForeignKey(Enfant, on_delete=models.CASCADE)
     Emplacement_id =models.ForeignKey(Emplacement, on_delete=models.CASCADE)

     class Meta:
        db_table = "Tache"
        verbose_name = "Tache"
        verbose_name_plural = "Taches"


class Rapport(models.Model):

    TextDate    = models.CharField(max_length=50)
    Problems    = models.CharField(blank=True , max_length=50)
    RapportDate = models.DateField(default=timezone.now)

    id_Tache    = models.OneToOneField(Tache, on_delete=models.CASCADE)

    class Meta:
        db_table = "Rapport"
        verbose_name = "Rapport"
        verbose_name_plural = "Rapports"





class Message(models.Model):
    Contenu = models.CharField(blank=False , max_length=256)
    Date    = models.DateField(default=timezone.now)


    id_enfant=models.ForeignKey(Enfant,on_delete=models.CASCADE)

    class Meta:
        db_table = "Message"
        verbose_name = "Message"
        verbose_name_plural = "Messages"