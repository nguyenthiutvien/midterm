import unittest
import first_test

class FirstTest(unittest.TestCase):
    def test_function(self):
        args = (2,4)
        self.assertEqual(first_test.tinhTong(*args),6)
        args=(2,3)
        self.assertEqual(first_test.tinhTong(*args),"Không phải 2 số chẵn")   

if __name__ =='__main__':
    unittest.main()


    