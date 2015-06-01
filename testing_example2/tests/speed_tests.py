from lib.light_calculator import calc_speed_of_light

import unittest

class TestLight(unittest.TestCase):

    def test_speed_ok(self):
        self.assertLess(5000, calc_speed_of_light())

