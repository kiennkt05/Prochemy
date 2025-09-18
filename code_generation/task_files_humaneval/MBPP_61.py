# MBPP/61
### Completion
def count_Substrings(s, n):
    count = 0
    
    # Iterate over all possible starting points of substrings
    for start in range(n):
        digit_sum = 0
        
        # Iterate over all possible ending points of substrings
        for end in range(start, n):
            # Convert the current character to an integer and add to digit_sum
            digit_sum += int(s[end])
            
            # Calculate the length of the current substring
            length = end - start + 1
            
            # Check if the sum of digits equals the length of the substring
            if digit_sum == length:
                count += 1
                
    return count

# Test case
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
