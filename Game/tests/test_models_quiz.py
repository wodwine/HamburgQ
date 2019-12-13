from django.test import TestCase 

from Game.models import Quiz,Question

class QuizTest(TestCase):
    
    def test_quiz_text(self):
        q1 = Quiz(quizz_name="Alpha")
        self.assertEqual(q1.__str__(),"Alpha")
        q2 = Quiz(quizz_name="Beta")
        self.assertEqual(q2.__str__(),"Beta")

    def test_question_count(self):
        q1 = Quiz(quizz_name="Alpha")
        q1.save()
        question1 = Question(question_text="What is this?",quizz_id = q1)
        question1.save()
        question2 = Question(question_text="Do you love him?",quizz_id = q1)
        question2.save()
        q1.save()
        self.assertEqual(2,q1.get_question_count())