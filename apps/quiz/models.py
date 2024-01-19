from django.db import models


# Create your models here.
class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1,
                                      choices=[
                                          ('A', 'Option 1'),
                                          ('B', 'Option 2'),
                                          ('C', 'Option 3'),
                                          ('D', 'Option 4')])

    objects = models.Manager()
