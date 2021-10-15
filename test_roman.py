import unittest
from roman import parseRoman, toRoman

class RomanNumeralTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(1, parseRoman('I'))
        self.assertEqual('I', toRoman(1))

    def test_two(self):
        self.assertEqual(2, parseRoman('II'))
        self.assertEqual('II', toRoman(2))

    def test_four(self):
        self.assertEqual(4, parseRoman('IV'))
        self.assertEqual('IV', toRoman(4))

    def test_five(self):
        self.assertEqual(5, parseRoman('V'))
        self.assertEqual('V', toRoman(5))

    def test_444(self):
        self.assertEqual(444, parseRoman('CDXLIV'))
        self.assertEqual('CDXLIV', toRoman(444))

    def test_555(self):
        self.assertEqual(555, parseRoman('DLV'))
        self.assertEqual('DLV', toRoman(555))

    def test_999(self):
        self.assertEqual(999, parseRoman('CMXCIX'))
        self.assertEqual('CMXCIX', toRoman(999))

    def test_1111(self):
        self.assertEqual(1111, parseRoman('MCXI'))
        self.assertEqual('MCXI', toRoman(1111))

    def test_3999(self):
        self.assertEqual(3999, parseRoman('MMMCMXCIX'))
        self.assertEqual('MMMCMXCIX', toRoman(3999))

    def test_zero(self):
        with self.assertRaises(ValueError):
            toRoman(0)
        with self.assertRaises(ValueError):
            parseRoman('')

    def test_4000(self):
        with self.assertRaises(ValueError):
            toRoman(4000)

    def test_iiii(self):
        with self.assertRaises(ValueError):
            parseRoman('IIII')

    def test_iviv(self):
        with self.assertRaises(ValueError):
            parseRoman('IVIV')

    def test_MMMM(self):
        with self.assertRaises(ValueError):
            parseRoman('MMMM')

    def test_float(self):
        with self.assertRaises(ValueError):
            toRoman(3.14)

    def test_Z(self):
        with self.assertRaises(ValueError):
            parseRoman('Z')
