# MBPP/386
### Completion
def swap_count(s: str) -> int:
    opening = 0  # Count of unmatched opening brackets
    closing = 0  # Count of unmatched closing brackets

    for char in s:
        if char == '[':
            opening += 1
        elif char == ']':
            if opening > 0:
                opening -= 1  # Match with an opening bracket
            else:
                closing += 1  # Unmatched closing bracket

    # The number of swaps needed is half the total unmatched brackets
    return (opening + closing) // 2

# Test the function with the provided assertion
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
