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
    answer = models.CharField(max_length=5,default="False")
    def __str__(self):
        return self.choice_text

class WaitingRoom(models.Model):
    room_name = models.CharField(max_length = 20)
    room_id = models.IntegerField(unique = True)
    quiz_type = models.ForeignKey(Quiz,on_delete= models.CASCADE,null = True)
    time = models.IntegerField(null=True)
    player = []
    def __str__(self):
        return self.room_name

class Player(models.Model):
    player_name = models.CharField(max_length = 20)
    room = models.ForeignKey(WaitingRoom, on_delete=models.CASCADE,null = True)
    score = models.IntegerField(default=0)
    current_question = models.IntegerField(default=0)
    def __str__(self):
        return self.player_name
    def progress(self):
        self.current_question += 1
        self.save()
    def add_score(self):
        self.score += 1
        self.save()
    
    