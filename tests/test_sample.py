import unittest


class TestSampleClass(unittest.TestCase):

    def test_should_fail(self):
        self.fail('You should remove this tests')


if __name__=="__main__":
    unittest.main()
