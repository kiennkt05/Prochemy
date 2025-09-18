# MBPP/386
### Completion
def swap_count(s: str) -> int:
    # Initialize counters for unmatched opening and closing brackets
    open_count = 0
    close_count = 0
    
    # Traverse the string to count unmatched brackets
    for char in s:
        if char == '[':
            open_count += 1
        elif char == ']':
            if open_count > 0:
                open_count -= 1  # Match with an opening bracket
            else:
                close_count += 1  # Unmatched closing bracket
    
    # The number of swaps needed is the number of unmatched closing brackets
    # since each swap can fix one unmatched closing bracket
    return (close_count + open_count) // 2

# Test case
assert swap_count("[]][][") == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert swap_count("[]][][") == 2
    assert swap_count("[[][]]") == 0
    assert swap_count("[[][]]][") == 1
