# MBPP/169
### Completion
def get_pell(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        pell_numbers = [0, 1]
        for i in range(2, n + 1):
            next_pell = 2 * pell_numbers[i - 1] + pell_numbers[i - 2]
            pell_numbers.append(next_pell)
        return pell_numbers[n]

# Test the function
assert get_pell(4) == 12
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_pell(4) == 12
    assert get_pell(7) == 169
    assert get_pell(8) == 408
