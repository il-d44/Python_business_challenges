import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Add the 'extracted' subfolder to the sys.path
extracted_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'extracted'))
sys.path.append(extracted_path)

# import function to test
from basic_extracted import calculator, format_checker, name_scorer

class Test_ExerciseOne(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calculator([7,12,-9], "add"), 10)
        self.assertEqual(calculator([10,5,5,25,7], "add"), 52)
        
    def test_sub(self):
        self.assertEqual(calculator([10,8], "subtract"), 2)
        self.assertEqual(calculator([50,50,50,-50,7,-7], "subtract"), 0)
    
    def test_mult(self):
        self.assertEqual(calculator([8,2,5,1,2], "multiply"), 160)
        self.assertEqual(calculator([-2, 1, -1, 1, -10], "multiply"), -20)
        
    def test_div(self):
        self.assertEqual(calculator([36,3,2,2], "divide"), 3.0)
        self.assertEqual(calculator([0,100,63,-17], "divide"), 0.0)
        
class Test_ExerciseTwo(unittest.TestCase):
    
    def test_invalid(self):
        self.assertEqual(format_checker('MoHHammed', 'T'), "Did you mean Mohhammed?")
        self.assertEqual(format_checker('ann', 'T'), "Did you mean Ann?")
        
    def test_tent(self):
        self.assertEqual(format_checker('Yuri', 'T'), "We hope to see you there, Yuri!")
        
    def test_acc(self):
        self.assertEqual(format_checker('Diana', 'A'), "Can't wait, Diana!")
        
    def test_deny(self):
        self.assertEqual(format_checker('Jasmine', 'D'), "Hope you can make it next time, Jasmine!")
        
class Test_ExerciseThree(unittest.TestCase):
    
    def test_basics(self):
        self.assertEqual(name_scorer('maybe?'), 82)
        self.assertEqual(name_scorer('name'), 80)
        
    def test_upps(self):
        self.assertEqual(name_scorer('HiHiIndie'), 95)
        self.assertEqual(name_scorer('MENACE!'), 80)
        self.assertEqual(name_scorer('kolaUp'), 85)
        
    def test_length(self):
        self.assertEqual(name_scorer('ol'), 74)
        self.assertEqual(name_scorer('underworldexperience'), 52)
        
    def test_special(self):
        self.assertEqual(name_scorer('TheXYZgame'), 86)
        self.assertEqual(name_scorer('Thexyzgame'), 91)
        self.assertEqual(name_scorer('theXYZgame'), 101)
        
    def test_chars(self):
        self.assertEqual(name_scorer('Awesome!!'), 85)
        self.assertEqual(name_scorer('&@$&*@!#?'), 45)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
