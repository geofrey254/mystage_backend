from django.db import models

# Create your models here.


class Road(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name


class Stop(models.Model):
    name = models.CharField(max_length=250, null=True)
    road = models.ForeignKey(Road, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Sacco(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name


class Stage(models.Model):
    name = models.CharField(max_length=250)
    route = models.ManyToManyField(Stop)
    sacco = models.ManyToManyField(Sacco)
    latitude = models.IntegerField()
    longitude = models.IntegerField()

    def __str__(self):
        return self.name + self.route.name
