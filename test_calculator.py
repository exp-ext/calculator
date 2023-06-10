import unittest

from calculator import PatternCalculator


class TestPatternCalculator(unittest.TestCase):
    def test_evaluate_volume(self):
        dict = {
            'длина': '10.5',
            'ширина': 15.5,
            'высота': 5,
        }
        pattern = 'объём | длина * ( ширина * высота ) + ( ширина + высота )'
        calc = PatternCalculator(dict, pattern)
        result = calc.evaluate()
        self.assertEqual(result[0], 'объём')
        self.assertEqual(result[1], 834.25)

    def test_evaluate_invalid_expression(self):
        dict = {
            'длина': '10.5',
            'ширина': 15.5,
            'высота': 5,
        }
        pattern = 'объём | длина + ширина * высота )'
        calc = PatternCalculator(dict, pattern)
        with self.assertRaises(ValueError):
            calc.evaluate()

    def test_evaluate_division_by_zero(self):
        """Если поле принимает в float, то 0 нужно запретить!"""
        dict = {
            'длина': '10.5',
            'ширина': '0',
            'высота': 5,
        }
        pattern = 'объём | длина * ( высота / ширина ) + ( ширина + высота )'
        calc = PatternCalculator(dict, pattern)
        with self.assertRaises(ZeroDivisionError):
            calc.evaluate()

    def test_another_pattern_test(self):
        dict = {
            'ось_x': '2',
            'ось_y': 4,
            'глубина': 5,
        }
        pattern = 'наличие | ось_x * ( ось_y * глубина ) + ( ось_y + глубина )'
        calc = PatternCalculator(dict, pattern)
        result = calc.evaluate()
        self.assertEqual(result[0], 'наличие')
        self.assertEqual(result[1], 49)


if __name__ == '__main__':
    unittest.main()
