# MBPP/539
### Completion
def basesnum_coresspondingnum(bases, exponents):
    """
    This function takes two lists: bases and exponents.
    It returns a list where each element is the base raised to the power of the corresponding exponent.
    
    Parameters:
    bases (list): A list of base numbers.
    exponents (list): A list of exponent numbers corresponding to each base.
    
    Returns:
    list: A list of results where each result is base[i] ** exponents[i].
    """
    # Using map to apply the power operation for each base and exponent
    result = list(map(lambda base, exp: base ** exp, bases, exponents))
    return result

# Test case
assert basesnum_coresspondingnum([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 
                                   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [
    10, 400, 27000, 2560000, 312500000, 46656000000, 
    8235430000000, 1677721600000000, 387420489000000000, 
    100000000000000000000
]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert basesnum_coresspondingnum([10, 20, 30, 40, 50, 60, 70, 80, 90, 100],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[10, 400, 27000, 2560000, 312500000, 46656000000, 8235430000000, 1677721600000000, 387420489000000000, 100000000000000000000]
    assert basesnum_coresspondingnum([1, 2, 3, 4, 5, 6, 7],[10, 20, 30, 40, 50, 60, 70])==[1, 1048576, 205891132094649, 1208925819614629174706176, 88817841970012523233890533447265625, 48873677980689257489322752273774603865660850176, 143503601609868434285603076356671071740077383739246066639249]
    assert basesnum_coresspondingnum([4, 8, 12, 16, 20, 24, 28],[3, 6, 9, 12, 15, 18, 21])==[64, 262144, 5159780352, 281474976710656, 32768000000000000000, 6979147079584381377970176, 2456510688823056210273111113728]
