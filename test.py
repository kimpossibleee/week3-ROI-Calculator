import unittest
from roi import RoiCalculator
from youtube_api import CallYoutubeAPI

class TestCalculator(unittest.TestCase):
    def test_calculator(self):
        my_calc = RoiCalculator()
        my_calc.initial_investment = 10000
        my_calc.yt_inflow = 40000
        my_calc.expenses = 10000
        my_calc.calculate_roi()
        result = my_calc.roi
        expected = 300
        self.assertEqual(result, expected)

    def test_youtube_api(self):
        my_api = CallYoutubeAPI()
        viewcount = my_api.call_yt_api('pewdiepie')
        result = 25000000000 < viewcount
        expected = True
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
