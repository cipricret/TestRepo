import unittest, mock
import ChessRules 
from ChessBoard import ChessBoard
from ChessGameParams import *
 
class CheckIsCheckmate(unittest.TestCase):



    @mock.patch('ChessGameParams.TkinterGameSetupParams.ok')
    def test_Player_Color(self, mockok):
        self.assertEqual(player1Color, "white")
        self.assertEqual(player2Color, "black")





 
 
if __name__=="__main__":
    unittest.main()
