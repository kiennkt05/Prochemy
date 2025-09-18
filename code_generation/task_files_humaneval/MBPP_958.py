# MBPP/958
### Completion
def int_to_roman(num):
    # Define a mapping of integers to Roman numerals
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    roman_numeral = ""
    i = 0
    # Iterate through the values and symbols
    while num > 0:
        # Determine how many times the current value fits into num
        for _ in range(num // val[i]):
            roman_numeral += syms[i]
            num -= val[i]
        i += 1  # Move to the next value/symbol pair
    
    return roman_numeral

# Test case
assert int_to_roman(1) == "I"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert int_to_roman(1)==("I")
    assert int_to_roman(50)==("L")
    assert int_to_roman(4)==("IV")
