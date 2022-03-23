from HelloWorld import sayHelloWorld
import unittest

class HelloWorldTest(unittest.TestCase):


    def testsayHelloWorld(self):
        self.assertEqual(sayHelloWorld(),"Hello World")


if __name__ == "__main__":
    unittest.main()