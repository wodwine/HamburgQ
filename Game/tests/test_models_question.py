from django.test import TestCase 

from Game.models import Question

class QuestionTest(TestCase):
    
    def test_Question_text(self):
        question1 = Question(question_text="What is this?")
        self.assertEqual(question1.__str__(),"What is this?")
        question2 = Question(question_text="Do you love him?")
        self.assertEqual(question2.__str__(),"Do you love him?")
    