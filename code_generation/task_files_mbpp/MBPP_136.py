# MBPP/136
### Completion
def cal_electbill(units):
    if units <= 50:
        bill = units * 1.50
    elif units <= 100:
        bill = (50 * 1.50) + ((units - 50) * 2.00)
    else:
        bill = (50 * 1.50) + (50 * 2.00) + ((units - 100) * 3.00)
    return bill

# Test the function with the provided assertion
assert cal_electbill(75) == 246.25
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert cal_electbill(75)==246.25
    assert cal_electbill(265)==1442.75
    assert cal_electbill(100)==327.5
