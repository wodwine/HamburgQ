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

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    def __str__(self):
        return self.choice_text

class WaitingRoom(models.Model):
    room_name = models.CharField(max_length = 20)
    room_id = models.IntegerField()
    class Meta:
        unique_together = ["room_name", "room_id"]
    def __str__(self):
        return room_name
    
    