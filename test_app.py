import unittest 
from app import say_hello

class TestApp(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello("AWS"),"hello, AWS")


        if__name:: == "__main__":
            unittest.main()