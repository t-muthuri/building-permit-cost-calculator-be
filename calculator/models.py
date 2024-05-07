from django.db import models

# Create your models here.


class County(models.Model):
  county_name = models.CharField(max_length=100)
  county_no = models.IntegerField(primary_key=True)
  
  def __str__(self):
        return self.county_name

class ProjectType(models.Model):
  project_name = models.CharField(max_length=100, default='Project Name')
  project_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
  county = models.ForeignKey(County, on_delete=models.CASCADE, default=0)
  
  
  def __str__(self):
        return self.project_name