from django.db import models

# Create your models here.

#Movies Name

class Movies(models.Model):
    
    name=models.CharField(max_length=50)
    year=models.CharField(max_length=20)
    hero=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=150, choices=(
                                             ('Hindi', 'Hind'),
                                             ('Telgu', 'Telgu'),
                                             ('Malyalam', 'Malyalam'),
                                              ('English', 'English')     
                                                   ))
    def __str__(self) -> str:
        return self.name 
    
class MoviesDetails(models.Model):
    name_id=models.AutoField(primary_key=True)
    director_name=models.CharField(max_length=100)
    collection=models.CharField(max_length=150)
    movies=models.ForeignKey(Movies, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name_id








