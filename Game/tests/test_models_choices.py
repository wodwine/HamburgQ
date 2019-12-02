from django.test import TestCase 

from Game.models import Choice

class ChoiceTest(TestCase):
    
    def test_choice_text(self):
        choice1 = Choice(choice_text="A")
        self.assertEqual(choice1.__str__(),"A")
        choice2 = Choice(choice_text="B")
        self.assertEqual(choice2.__str__(),"B")
        choice3 = Choice(choice_text="C")
        self.assertEqual(choice3.__str__(),"C")
        choice4 = Choice(choice_text="D")
        self.assertEqual(choice4.__str__(),"D")
    