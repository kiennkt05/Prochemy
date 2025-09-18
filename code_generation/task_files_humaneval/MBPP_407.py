# MBPP/407
### Completion
def rearrange_bigger(n):
    # Convert the number to a list of its digits
    digits = list(str(n))
    length = len(digits)

    # Step 1: Find the rightmost ascent
    i = length - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    # If no ascent is found, return -1 (no bigger number possible)
    if i == -1:
        return -1

    # Step 2: Find the smallest digit on the right side of the ascent that is larger than digits[i]
    j = length - 1
    while digits[j] <= digits[i]:
        j -= 1

    # Step 3: Swap the found digits
    digits[i], digits[j] = digits[j], digits[i]

    # Step 4: Reverse the sequence after the position i
    digits = digits[:i + 1] + digits[i + 1:][::-1]

    # Convert back to integer
    return int(''.join(digits))

# Test case
assert rearrange_bigger(12) == 21
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert rearrange_bigger(12)==21
    assert rearrange_bigger(10)==False
    assert rearrange_bigger(102)==120
