import os
import sys
import unittest


# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Add the 'extracted' subfolder to the sys.path
extracted_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'extracted'))
sys.path.append(extracted_path)

from medium_extracted import earnings_calculator, check_number, username_generator

class Test_ExerciseOne(unittest.TestCase):
    
    def test_invalid(self):
        self.assertEqual(earnings_calculator(''), "Invalid input")
        self.assertEqual(earnings_calculator([89253, 1890, 66620, 77129, 10000]), "Invalid input")
        self.assertEqual(earnings_calculator([15000, 18000, 22000, 'apple']), "Invalid input")
    
    def test_notax(self):
        self.assertEqual(earnings_calculator([0,0,1000,2000]), 3000.0)
        self.assertEqual(earnings_calculator([15000,15000,15000,15000]), 60000.0)
    
    def test_brackets(self):
        self.assertEqual(earnings_calculator([16000, 29000, 53900, 33000]), 114615.0)
        self.assertEqual(earnings_calculator([25000, 25000, 25000, 35000]), 101700.0)

class Test_ExerciseTwo(unittest.TestCase):
    
    def test_invalid(self):
        self.assertEqual(check_number([7623]), "Invalid number!")
        self.assertEqual(check_number('0896231'), "Invalid number!")
        self.assertEqual(check_number('0628792690'), "Invalid number!")
    
    def test_generic(self):
        self.assertEqual(check_number('067982'), "Your number is great! You have a business number.")
        self.assertEqual(check_number('099882'), "Your number is great! You have a business number.")
        self.assertEqual(check_number('072358811'), "Your number is great! You have a classic number.")
        self.assertEqual(check_number('0764321690'), "Your number is great! You have a classic number.")
        
    def test_digits(self):
        self.assertEqual(check_number('0712345698'), "Wow, your number contains all 10 digits! You have a classic number.")
        self.assertEqual(check_number('0784215963'), "Wow, your number contains all 10 digits! You have a classic number.")
        
    def test_repeat(self):
        self.assertEqual(check_number('055456'), "Your number contains the digit 5 at least 3 times! You have a business number.")
        self.assertEqual(check_number('079908629'), "Your number contains the digit 9 at least 3 times! You have a classic number.")
        
    def test_streak(self):
        self.assertEqual(check_number('022789'), "You have a consecutive streak in your number ;) You have a business number.")
        self.assertEqual(check_number('0719073456'), "You have a consecutive streak in your number ;) You have a classic number.")
        self.assertEqual(check_number('075212399'), "You have a consecutive streak in your number ;) You have a classic number.")
        
class Test_ExerciseThree(unittest.TestCase):
    
    def test_simple(self):
        self.assertEqual(username_generator([('Kelly', 'Kotse'), 1995]), "K_kotse95")
        self.assertEqual(username_generator([('Cooper', 'Muipo'), 1972]), "C_muipo72")
        
    def test_dup(self):
        self.assertEqual(username_generator([('Ferdy', 'Phones'), 1984, 52]), "F_phones84_52")
        self.assertEqual(username_generator([('Karl', 'Mings'), 2010, 6]), "K_mings10_6")
        
    def test_swaps(self):
        self.assertEqual(username_generator([1911, ('Valerion', 'Lindz')]), "V_lindz11")
        self.assertEqual(username_generator([1999, 99, ('Kort', 'Elisan')]), "K_elisan99_99")
        self.assertEqual(username_generator([('Tyrion', 'Axel'), 12, 2007]), "T_axel07_12")
        self.assertEqual(username_generator([0, ('Yuri', 'Heverin'), 1992]), "Y_heverin92_0")

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
