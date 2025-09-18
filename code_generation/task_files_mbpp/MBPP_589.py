# MBPP/589
### Completion
def perfect_squares(start, end):
    """Return a list of perfect squares between start and end (inclusive)."""
    squares = []
    for i in range(int(start**0.5), int(end**0.5) + 1):
        square = i * i
        if start <= square <= end:
            squares.append(square)
    return squares

# Test the function with the provided assertion
assert perfect_squares(1, 30) == [1, 4, 9, 16, 25]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
    assert perfect_squares(50,100)==[64, 81, 100]
    assert perfect_squares(100,200)==[100, 121, 144, 169, 196]
