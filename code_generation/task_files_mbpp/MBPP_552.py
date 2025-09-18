# MBPP/552
### Completion
def Seq_Linear(sequence):
    if len(sequence) < 2:
        return "Linear Sequence"  # A sequence with less than 2 elements is trivially linear

    # Calculate the common difference
    common_difference = sequence[1] - sequence[0]

    # Check if all consecutive differences are the same
    for i in range(1, len(sequence) - 1):
        if sequence[i + 1] - sequence[i] != common_difference:
            return "Not a Linear Sequence"

    return "Linear Sequence"

# Test the function with the provided assertion
assert Seq_Linear([0, 2, 4, 6, 8, 10]) == "Linear Sequence"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Seq_Linear([0,2,4,6,8,10]) == "Linear Sequence"
    assert Seq_Linear([1,2,3]) == "Linear Sequence"
    assert Seq_Linear([1,5,2]) == "Non Linear Sequence"
