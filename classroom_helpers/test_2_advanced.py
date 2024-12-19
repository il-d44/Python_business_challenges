import os
import sys
import unittest


# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Add the 'extracted' subfolder to the sys.path
extracted_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'extracted'))
sys.path.append(extracted_path)

from advanced_extracted import check_name, check_password

class Test_ExerciseOne(unittest.TestCase):
    
    def test_empty(self):
        self.assertEqual(check_name(''), "This is a compulsory field")
        
    def test_basic(self):
        self.assertEqual(check_name('Alex Caian'), "OK")
        self.assertEqual(check_name('Lisa Carpenter Joanne'), "OK")
        self.assertEqual(check_name('Roger-Nigel Hendrich Tuluz Fonfor Fancy-Name Lu Xi Yo'), "OK")
        
    def test_invalids(self):
        self.assertEqual(check_name('E E E'), "Invalid name")
        self.assertEqual(check_name(['John', 'Smith']), "Invalid name")
        self.assertEqual(check_name(55), "Invalid name")
        
    def test_capitals(self):
        self.assertEqual(check_name('hector jubilantes'), "Did you mean Hector Jubilantes?")
        self.assertEqual(check_name('Diana Ray sofia'), "Did you mean Diana Ray Sofia?")

class Test_ExerciseTwo(unittest.TestCase):
    
    def test_invalid(self):
        self.assertEqual(check_password('A', 86272), "Invalid password")
        self.assertEqual(check_password('A', '9B![>aloes'), "Invalid password")
        self.assertEqual(check_password('B', ('{&*@$!@|KL', 72590, 'apple')), "Invalid pair")
        self.assertEqual(check_password('B', ['#$.,><><', '66230']), "Invalid pair")
        
    def test_correct(self):
        self.assertEqual(check_password('A', 'Hello123!>.<'), "Connection OK")
        self.assertEqual(check_password('A', 'aLo&.3'), "Connection OK")
        self.assertEqual(check_password('A', 'VerifyMe!99;'), "Connection OK")
        self.assertEqual(check_password('B', ('#$*@!>\|PO', '88898')), "Connection OK")
        self.assertEqual(check_password('B', ('".<)()??ZZ', 54102)), "Connection OK")
        
    def test_long(self):
        self.assertEqual(check_password('A', 'Ty89??AH*DSJDSOJDIYUSIHfy7yigfr567/u2[]'), "Password length incorrect")
        self.assertEqual(check_password('A', 'M!?'), "Password length incorrect")
        
    def test_missing(self):
        self.assertEqual(check_password('A', 'HelloThere'), "Missing 2 character(s) of type special character Missing 1 character(s) of type digit ")
        self.assertEqual(check_password('A', 'applesbanana'), "Missing 2 character(s) of type special character Missing 1 character(s) of type digit Missing 1 character(s) of type uppercase ")
        self.assertEqual(check_password('A', '!!!!!!!!!!!!'), "Missing 1 character(s) of type digit Missing 1 character(s) of type uppercase ")
        
    def test_key(self):
        self.assertEqual(check_password('B', ('0?!@&&{}LP', 88104)), "Incorrect key")
        self.assertEqual(check_password('B', ('%$@@~`**Lz', 10020)), "Incorrect key")
        self.assertEqual(check_password('B', ('^%??~!!;.MA', 96520.0)), "Incorrect key")
        
    def test_value(self):
        self.assertEqual(check_password('B', ('%@^!#@><II', 9898)), "Incorrect value")
        self.assertEqual(check_password('B', ('%@^!#@><II', 89359283)), "Incorrect value")
        self.assertEqual(check_password('B', ('%@^!#@><II', 'apple')), "Incorrect value")

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
