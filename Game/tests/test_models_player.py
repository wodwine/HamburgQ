from django.test import TestCase 

from Game.models import WaitingRoom,Player

class PlayerTest(TestCase):

    def test_add_and_reset_socre(self):
        """test add_score and reset score function"""
        player = Player(player_name = "test")
        player.add_score()
        self.assertEqual(player.score,1)
        player.reset_score()
        self.assertEqual(player.score,0)
        player.score = 500
        player.save()
        player.reset_score()
        self.assertEqual(player.score,0)

    def test_progress(self):
        """test the progress function"""
        player = Player(player_name = "test")
        player.progress()
        self.assertEqual(player.current_question,1)
        self.assertEqual(player.score,0)
        player.score = 500
        player.save()
        player.progress()
        self.assertEqual(player.current_question,2)
        self.assertEqual(player.streak,500)
        #when score is lower than streak
        player.score = 300
        player.save()
        player.progress()
        self.assertEqual(player.streak,500)
        self.assertEqual(player.score,300)
        #when score is higher than streak
        player.score = 1000
        player.save()
        player.progress()
        self.assertEqual(player.streak,1000)

    def test_name(self):
        """Test the name of the player"""
        player = Player(player_name = "test")
        self.assertEqual(player.__str__(),"test")
        player = Player(player_name = "wine")
        self.assertEqual(player.__str__(),"wine")

