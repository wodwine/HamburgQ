from django.db import models
from django.utils import timezone
import datetime
import logging

LOG_FILE_NAME = 'HamburQ.log'

def configure_log(log_name:str):
    """configure logger and log with name = argument"""
    filehandler = logging.FileHandler(log_name)
    root = logging.getLogger()
    root.setLevel( logging.NOTSET )
    filehandler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        'time:%(asctime)s from "%(name)s" level:%(levelname)s -- %(message)s'
        )
    filehandler.setFormatter(formatter)
    root = logging.getLogger()
    root.addHandler(filehandler)

class Quiz(models.Model):
    quizz_name = models.CharField(max_length=200)

    def __str__(self):
        return self.quizz_name
    
    def get_question_count(self):
        return len(self.question_set.all())


class Question(models.Model):
    quizz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text
    



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    answer = models.BooleanField(default=0)

    def __str__(self):
        return self.choice_text

class WaitingRoom(models.Model):
    room_name = models.CharField(max_length = 20)
    room_id = models.IntegerField(unique = True)
    quiz_type = models.ForeignKey(Quiz,on_delete= models.CASCADE,null = True)
    time = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    started = models.BooleanField(default=0)

    def __str__(self):
        return self.room_name
        
    def get_time_over(self):
        #add two second to let program chtach up
        return self.created + datetime.timedelta(seconds=(self.time * len(self.quiz_type.question_set.all()) - 2))

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
    is_logged = models.BooleanField(default=0)

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

    def log(self):
        if not self.is_logged:
            configure_log(LOG_FILE_NAME)
            logger = logging.getLogger()
            logger.info(f"{self.player_name} login room with id {self.room.room_id}")
            self.is_logged = 1
            self.save()
    
    