import unittest
import rome_digits


class RomeDigitsTest(unittest.TestCase):

    def test_all_digits(self):
        digits = ("I", "V", "X", "L", "C", "M")
        for value in digits:
            res = rome_digits.simply_check(value)
            self.assertEqual(res, True)

    def test_8(self):
        res = rome_digits.simply_parse_rome_digit("VIII")
        self.assertEqual(res, 8)

    def test_9(self):
        res = rome_digits.simply_parse_rome_digit("IX")
        self.assertEqual(res, 9)

    def test_3(self):
        res = rome_digits.simply_parse_rome_digit("III")
        self.assertEqual(res, 3)

    def test_97(self):
        res = rome_digits.simply_parse_rome_digit("XCVII")
        self.assertEqual(res, 97)

    def test_98(self):
        res = rome_digits.simply_parse_rome_digit("XCVIII")
        self.assertEqual(res, 98)

    def test_70_is_bad(self):
        # XXL - некорректное значение
        res = rome_digits.simply_parse_rome_digit("XXL")
        self.assertEqual(res, 50)

    def test_15_is_bad(self):
        # XIIV - некорректное значение
        res = rome_digits.simply_parse_rome_digit("XIIV")
        self.assertEqual(res, 15)

    def test_3949(self):
        res = rome_digits.simply_parse_rome_digit("MMMCMXLIX")
        self.assertEqual(res, 3949)

    def test_3499(self):
        res = rome_digits.simply_parse_rome_digit("MMMCDXCIX")
        self.assertEqual(res, 3499)

    def test_3999(self):
        res = rome_digits.simply_parse_rome_digit("MMMCMXCIX")
        self.assertEqual(res, 3999)


if __name__ == "__main__":
    unittest.main()


