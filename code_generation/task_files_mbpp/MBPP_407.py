# MBPP/407
### Completion
def rearrange_bigger(n):
    # Convert the number to a list of its digits
    digits = list(str(n))
    
    # Step 1: Find the first decreasing element from the right
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    
    # If no such element is found, return the original number
    if i == -1:
        return n
    
    # Step 2: Find the element just larger than digits[i] to the right of it
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    
    # Step 3: Swap the found elements
    digits[i], digits[j] = digits[j], digits[i]
    
    # Step 4: Reverse the sequence after the position i
    digits = digits[:i + 1] + digits[i + 1:][::-1]
    
    # Convert the list of digits back to an integer
    return int(''.join(digits))

# Test the function with the provided assertion
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
