# MBPP/684
### Completion
def count_Char(s: str, char: str, n: int) -> int:
    """
    Count occurrences of a character in a repeated string.

    Parameters:
    s (str): The base string to be repeated.
    char (str): The character to count in the repeated string.
    n (int): The number of times the base string is repeated.

    Returns:
    int: The total occurrences of the character in the repeated string.
    """
    # Count occurrences of char in the base string
    count_in_s = s.count(char)
    
    # Total occurrences in the repeated string
    total_count = count_in_s * n
    
    return total_count

# Example usage
base_string = "abcac"
character_to_count = 'a'
repetitions = 4  # Assuming we want to repeat the string 4 times

# Calculate the total occurrences
result = count_Char(base_string, character_to_count, repetitions)
print(result)  # Output should be 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Char("abcac",'a') == 4
    assert count_Char("abca",'c') == 2
    assert count_Char("aba",'a') == 7
