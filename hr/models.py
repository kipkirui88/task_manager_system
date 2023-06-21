from django.contrib.auth.models import AbstractUser, User
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Superuser'),
        (2, 'HR'),
        (3, 'Employee'),
    )
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES, default=1)


class Employees(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, default=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.IntegerField()
    gender = models.CharField(max_length=100, choices=GENDER)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    dor = models.DateField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Employees'

class Tasks(models.Model):
    STATUS = (
        ('To DO', 'To DO'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS)
    start_date = models.DateField()
    due_date = models.DateField()


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Tasks"
