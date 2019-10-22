from django.db import models

class Quiz(models.Model):
    quizz_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.quizz_name

class Question(models.Model):
    quizz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text
