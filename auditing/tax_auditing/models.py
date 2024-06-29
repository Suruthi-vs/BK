from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Email(models.Model):
    email_id = models.EmailField()
    subject = models.CharField(max_length=100)
    description = models.TextField()
