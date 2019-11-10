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
    # quizz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    def __str__(self):
        return self.choice_text

class WaitingRoom(models.Model):
    room_name = models.CharField(max_length = 20)
    room_id = models.IntegerField(unique = True)
    quiz_type = models.ForeignKey(Quiz,on_delete= models.CASCADE,null = True)
    time = models.IntegerField(null=True)
    player = []
    def __str__(self):
        return room_name

class Player(models.Model):
    player_name = models.CharField(max_length = 20)
    room_id_player = models.IntegerField()
    def __str__(self):
        return player_name
    
    