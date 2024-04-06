from unittest import TestCase, main
from main import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('10-2'), 8)

    def test_multiply(self):
        self.assertEqual(calculator('2*7'), 14)

    def test_divide(self):
        self.assertEqual(calculator('10/2'), 5)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator("qwerty")
        self.assertEqual('Выражение должно содерджать хотя бы один знак +-*/', e.exception.args[0])

    def test_to_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator("2+2+2")
        self.assertEqual('Выражение должно содержать 2 целые числа и 1 знак', e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator("2+5+10")
        self.assertEqual('Выражение должно содержать 2 целые числа и 1 знак', e.exception.args[0])

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator("3.1+0.3")
        self.assertEqual('Выражение должно содержать 2 целые числа и 1 знак', e.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator("a+b")
        self.assertEqual('Выражение должно содержать 2 целые числа и 1 знак', e.exception.args[0])


if __name__ == '__main__':
    main()
