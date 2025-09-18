# MBPP/552
### Completion
def Seq_Linear(sequence):
    # Check if the sequence has fewer than 2 elements
    if len(sequence) < 2:
        return "Linear Sequence"
    
    # Calculate the common difference
    common_difference = sequence[1] - sequence[0]
    
    # Check the difference between each pair of consecutive elements
    for i in range(1, len(sequence) - 1):
        if (sequence[i + 1] - sequence[i]) != common_difference:
            return "Not a Linear Sequence"
    
    return "Linear Sequence"

# Test case
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
