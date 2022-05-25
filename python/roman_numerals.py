def to_roman(num):
    roman_result = ''
    roman_to_arabic = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1,
    }

    while num > 0:
        for key in roman_to_arabic:
            if num / roman_to_arabic[key] >= 1:
                roman_result += key
                num -= roman_to_arabic[key]
                break;
                
    return roman_result


#print(to_roman(27))