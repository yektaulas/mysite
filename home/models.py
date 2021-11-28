from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    departments = [
        ('GE', 'General'),
        ('HI', 'Hire'),

    ]

    dept = models.CharField(max_length=2, choices=departments, default=departments[0][0])
