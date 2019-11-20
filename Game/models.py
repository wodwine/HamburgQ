from django.db import models
from django.utils import timezone
import datetime

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
    answer = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class WaitingRoom(models.Model):
    room_name = models.CharField(max_length = 20)
    room_id = models.IntegerField(unique = True)
    quiz_type = models.ForeignKey(Quiz,on_delete= models.CASCADE,null = True)
    time = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    started = models.BooleanField(default=False)

    def __str__(self):
        return self.room_name
        
    def get_time_over(self):
        return self.created + datetime.timedelta(seconds=(self.time * len(self.quiz_type.question_set.all())))

    def time_over(self):
        # datetime.timedelta will always display negative time with -days
        if (timezone.now() - self.get_time_over()).days <= -1:
            return False
        return True
    
    def reset_create(self):
        self.created = timezone.now()
        self.save()

class Player(models.Model):
    status = models.CharField(max_length = 20,default="Player")
    player_name = models.CharField(max_length = 20)
    room = models.ForeignKey(WaitingRoom, on_delete=models.CASCADE,null = True)
    score = models.IntegerField(default=0)
    current_question = models.IntegerField(default=0)
    streak = models.IntegerField(default=0)
    
    def __str__(self):
        return self.player_name

    def reset_score(self):
        self.score = 0
        self.save()

    def progress(self):
        self.current_question += 1
        if self.score > self.streak:
            self.streak = self.score
        self.save()

    def add_score(self):
        self.score += 1
        self.save()
    
    