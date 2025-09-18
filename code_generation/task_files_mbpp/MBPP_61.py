# MBPP/61
### Completion
def count_Substrings(s, n):
    count = 0
    length = len(s)
    
    # Iterate through all possible substrings
    for i in range(length):
        for j in range(i + 1, length + 1):
            substring = s[i:j]
            digit_sum = sum(int(char) for char in substring)
            substring_length = len(substring)
            
            # Check if the sum of digits equals the length of the substring
            if digit_sum == substring_length:
                count += 1
                
    return count

# Test the function with the provided assertion
assert count_Substrings('112112', 6) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Substrings('112112',6) == 6
    assert count_Substrings('111',3) == 6
    assert count_Substrings('1101112',7) == 12
