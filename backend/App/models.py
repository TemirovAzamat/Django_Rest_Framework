from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=30)
    work_experience = models.IntegerField()

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=30)
    visit = models.CharField(max_length=30)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
