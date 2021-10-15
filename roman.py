table = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
}

max_repeats = {
    1000: 3,
    900: 1,
    500: 1,
    400: 1,
    100: 3,
    90: 1,
    50: 1,
    40: 1,
    10: 3,
    9: 1,
    5: 1,
    4: 1,
    1: 3,
}

def _parseDigit(roman, number, value, rdigit):
    repeats = 0
    while roman.startswith(rdigit):
        number += value
        roman = roman[len(rdigit):]
        repeats += 1
    if repeats > max_repeats[value]:
        raise ValueError()
    return roman, number

def parseRoman(roman):
    number = 0
    if roman == '':
        raise ValueError()
    for value, rdigit in table.items():
        roman, number = _parseDigit(roman, number, value, rdigit)
    if roman != '':
        raise ValueError()
    return number

def _toRoman(roman, number, value, rdigit):
    while number >= value:
        roman += rdigit
        number -= value
    return roman, number

def toRoman(number):
    if not isinstance(number, int):
        raise ValueError()
    roman = ''
    if number < 1 or number > 3999:
        raise ValueError()
    for value, rdigit in table.items():
        roman, number = _toRoman(roman, number, value, rdigit)
    return roman
