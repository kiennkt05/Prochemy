# MBPP/417
### Completion
def group_tuples(tuples_list):
    from collections import defaultdict

    # Create a dictionary to hold lists of second elements grouped by the first element
    grouped = defaultdict(list)

    # Iterate through the list of tuples
    for first, second in tuples_list:
        grouped[first].append(second)

    # Create the result list
    result = []
    for first, seconds in grouped.items():
        # Create a tuple with the first element and the corresponding second elements
        result.append((first, *seconds))

    return result

# Test the function with the provided assertion
assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]
