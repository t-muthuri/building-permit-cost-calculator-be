from django.db import models

# Create your models here.
class ProjectType(models.Model):
  project_label = models.CharField(max_length=100)  

  def __str__(self):
        return self.project_label

class County(models.Model):
  county_name = models.CharField(max_length=100)
  county_no = models.IntegerField(primary_key=True)
  county_price = models.DecimalField(max_digits=6, decimal_places=2)
  
  def __str__(self):
        return self.county_name