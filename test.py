import unittest
from unittest import mock
from sample_tray import getAdjacentPositiveSamples


class Test(unittest.TestCase):
    @mock.patch('sample_tray.input', create=True)
    def test_sample_input_one(self,mocked_input):
        mocked_input.side_effect = [3, 8, "1 0 1 1 0 1 1 1 0 1 1 0 0 1 1 0 1 1 0 0 1 1 1 0"]
        result = getAdjacentPositiveSamples()
        self.assertEqual(
            result, 
            {0: [[2, 3], [5, 6, 7]], 1: [[1, 2], [5, 6]], 2: [[0, 1], [4, 5, 6]]}
        )

    @mock.patch('sample_tray.input', create=True)
    def test_sample_input_two(self,mocked_input):
        mocked_input.side_effect = [5, 5, "0 1 1 1 1 1 0 0 1 1 0 0 0 0 1 1 0 1 0 1 0 1 1 0 0"]
        result = getAdjacentPositiveSamples()
        self.assertEqual(
            result, 
            {0: [[1, 2, 3, 4]], 1: [[3, 4]], 2: [], 3: [], 4: [[1, 2]]}
        )

    @mock.patch('sample_tray.input', create=True)
    def test_sample_input_three(self,mocked_input):
        mocked_input.side_effect = ['hello', 'World', "Hi"]
        with self.assertRaises(ValueError):
            getAdjacentPositiveSamples()

    @mock.patch('sample_tray.input', create=True)
    def test_sample_input_three(self,mocked_input):
        mocked_input.side_effect = [3, 3, "1 0 1 0 1"]
        with self.assertRaises(Exception):
            getAdjacentPositiveSamples()


if __name__ == '__main__':
    unittest.main()