from django.db import models

# Create your models here.


class County(models.Model):
    county_name = models.CharField(max_length=100)
    county_no = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.county_name


class ProjectType(models.Model):
    project_type_name = models.CharField(max_length=100, default='Commercial')
    project_type_no = models.IntegerField(primary_key=True, default=1)

    def __str__(self):
        return self.project_type_name
