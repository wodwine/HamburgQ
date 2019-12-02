import datetime

from django.test import TestCase 

from Game.models import WaitingRoom,Quiz

class WaitingRoomTests(TestCase):

    def test_time_over_after_a_year(self):
        """test time over on a one year old quiz"""
        q = Quiz(quizz_name = "test_quiz")
        q.save()
        q.question_set.create(question_text = "test_question")
        q.save()
        wr = WaitingRoom(room_name = "test_room",
                        room_id = 123456,time = 5,
                        quiz_type = q)
        wr.reset_create()
        wr.created -= datetime.timedelta(days=365)
        wr.save()
        self.assertIs(wr.time_over(),True)

    def test_before_time_over(self):
        """test when the time isn't over yet"""
        q = Quiz(quizz_name = "test_quiz")
        q.save()
        q.question_set.create(question_text = "test_question")
        q.save()
        wr = WaitingRoom(room_name = "test_room",
                         room_id = 123456,time = 150,
                         quiz_type = q)
        wr.reset_create()
        wr.save()
        self.assertIs(wr.time_over(),False)