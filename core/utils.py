# Creado Por Armando Ruiz Rebollar

def roman_integer_conversion(whole):
    numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    numeral = ''
    i = 0

    while whole > 0:
        for _ in range(whole // numbers[i]):
            numeral += numerals[i]
            whole -= numbers[i]

        i += 1

    return numeral
