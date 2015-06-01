import unittest

class TestB(unittest.TestCase):
    
    def setUp(self):  # Special name of unit test set up - runs before EVERY test
        self.my_array = [1,2,3,4,5]

    def tearDown(self):  # Special name
        self.my_array = None

    def test_adel(self):
        del self.my_array[1]
        self.assertEqual(4, len(self.my_array))
        
    def check_length(self):  # utility 
        self.assertEqual(5, len(self.my_array))
        
    def test_count(self):
        self.check_length()

    def test_count_again(self):
        self.my_array.pop()
        self.my_array.append(99)
        self.check_length()
    
#suite = unittest.TestLoader().loadTestsFromTestCase(TestB)
#unittest.TextTestRunner(verbosity=2).run(suite)
