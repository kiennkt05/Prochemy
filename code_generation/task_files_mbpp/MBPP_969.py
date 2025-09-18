# MBPP/969
### Completion
def join_tuples(tuples):
    from collections import defaultdict

    # Create a dictionary to hold lists of tuples by their first element
    grouped = defaultdict(list)

    # Group tuples by their first element
    for t in tuples:
        grouped[t[0]].append(t[1])

    # Create the result list by joining the first element with the corresponding values
    result = []
    for key, values in grouped.items():
        result.append((key,) + tuple(values))

    return result

# Test the function with the provided assertion
assert join_tuples([(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]) == [(5, 6, 7), (6, 8, 10), (7, 13)]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert join_tuples([(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)] ) == [(5, 6, 7), (6, 8, 10), (7, 13)]
    assert join_tuples([(6, 7), (6, 8), (7, 9), (7, 11), (8, 14)] ) == [(6, 7, 8), (7, 9, 11), (8, 14)]
    assert join_tuples([(7, 8), (7, 9), (8, 10), (8, 12), (9, 15)] ) == [(7, 8, 9), (8, 10, 12), (9, 15)]
