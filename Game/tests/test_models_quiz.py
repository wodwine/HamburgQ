from django.test import TestCase 

from Game.models import Quiz

class QuizTest(TestCase):
    
    def test_quiz_text(self):
        q1 = Quiz(quizz_name="Alpha")
        self.assertEqual(q1.__str__(),"Alpha")
        q2 = Quiz(quizz_name="Beta")
        self.assertEqual(q2.__str__(),"Beta")
    