# MBPP/969
### Completion
def join_tuples(tuples):
    from collections import defaultdict

    # Step 1: Group tuples by their first element
    grouped = defaultdict(list)
    for t in tuples:
        grouped[t[0]].append(t[1])

    # Step 2: Create the result list by combining the first element with its grouped values
    result = []
    for key, values in grouped.items():
        # Combine the key with the values
        combined_tuple = (key,) + tuple(values)
        result.append(combined_tuple)

    # Step 3: Return the result
    return result

# Test case
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
