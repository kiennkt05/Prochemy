# MBPP/684
### Completion
def count_Char(s, char, n):
    # Count occurrences of char in the original string
    count_in_s = s.count(char)
    
    # Calculate how many times the string is repeated
    full_repeats = n // len(s)
    
    # Count occurrences in the full repeats
    total_count = full_repeats * count_in_s
    
    # Count occurrences in the remaining part of the string
    remainder = n % len(s)
    total_count += s[:remainder].count(char)
    
    return total_count

# Example usage
repeated_string = "abcac"
n = 10  # Length of the repeated string
char_to_count = 'a'
result = count_Char(repeated_string, char_to_count, n)
assert result == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Char("abcac",'a') == 4
    assert count_Char("abca",'c') == 2
    assert count_Char("aba",'a') == 7
