class IntegerToRoman:
    def __init__(self, number):
        if not isinstance(number, int):
            raise TypeError("Input must be an integer.")
        if not (1 <= number <= 3999):
            raise ValueError("Number must be between 1 and 3999 inclusive.")
        self.number = number
        self.value_symbols = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

    def convert(self):
        num = self.number
        roman_numeral = ""
        for value, symbol in self.value_symbols:
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral


if __name__ == "__main__":
    try:
        num1 = IntegerToRoman(1994)
        print(num1.convert())

        num2 = IntegerToRoman(58)
        print(num2.convert())

        num3 = IntegerToRoman(3999)
        print(num3.convert())
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")