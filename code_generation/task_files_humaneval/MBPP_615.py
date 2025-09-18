# MBPP/615
### Completion
def average_tuple(tuples):
    # Check if the input is empty
    if not tuples:
        return []
    
    # Get the number of inner tuples
    num_tuples = len(tuples)
    
    # Get the number of elements in the first inner tuple
    num_elements = len(tuples[0])
    
    # Initialize a list to hold the sum of each index
    sums = [0] * num_elements
    
    # Iterate through each tuple and sum the values at each index
    for tup in tuples:
        for i in range(num_elements):
            sums[i] += tup[i]
    
    # Calculate the average for each index
    averages = [s / num_tuples for s in sums]
    
    return averages

# Test the function with the provided test case
assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))) == [30.5, 34.25, 27.0, 23.25]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))==[30.5, 34.25, 27.0, 23.25]
    assert average_tuple(((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3)))== [25.5, -18.0, 3.75]
    assert average_tuple( ((100, 100, 100, 120), (300, 450, 560, 450), (810, 800, 390, 320), (10, 20, 30, 40)))==[305.0, 342.5, 270.0, 232.5]
