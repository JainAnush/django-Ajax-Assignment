from django.db import models

class quiz(models.Model):
    question_id=models.IntegerField(primary_key=True)
    question=models.TextField()
    option1=models.TextField()
    option2=models.TextField()
    option3=models.TextField()
    option4=models.TextField()
    correctans=models.IntegerField()
