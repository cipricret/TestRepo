import unittest, mock
import ChessRules 

class testMisc(unittest.TestCase):

    @mock.patch('ChessRules.ChessRules.IsCheckmate')
    
    def test_color(self, enemyColor):
        self.assertNotEqual(enemyColor, enemyColor)



if __name__=="__main__":
    unittest.main()
