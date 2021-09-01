from django.db import models
from django.urls import reverse

# Create your models here.

# HOME SECTION

class Home(models.Model):
    name = models.CharField(max_length=50)
    intro = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='picture/')
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ABOUT SECTION

class About(models.Model):
    heading = models.CharField(max_length=50)
    description = models.TextField(blank=False)

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading

# Experience SECTION

class Experience(models.Model):
    workplace_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, default='')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.workplace_name

class JobDescription(models.Model):
    experience = models.ForeignKey(Experience,
                                 on_delete=models.CASCADE)
    job_responsibility = models.CharField(max_length=200, blank=False, default='')

# SKILLS SECTION

class Category(models.Model):
    name = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name



class Skills(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50)


# Projects SECTION

class Project(models.Model):
    project_name = models.CharField(max_length=100, default='DEFAULT VALUE')
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.project_name