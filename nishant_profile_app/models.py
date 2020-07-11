from django.db import models


# Create your models here.

class ProjectApplication(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class ProjectAppsUse(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class ProjectCourse(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class ProjectHabit(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
