# MBPP/71
### Completion
def comb_sort(arr):
    """Sorts a list using the comb sort algorithm."""
    gap = len(arr)
    shrink = 1.3
    sorted = False

    while not sorted:
        # Update the gap for the next comb
        gap = max(1, int(gap / shrink))
        sorted = True

        # Compare elements at the current gap
        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                # Swap the elements
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False

    return arr

# Test the comb_sort function
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
    assert comb_sort([41, 32, 15, 19, 22]) == [15, 19, 22, 32, 41]
    assert comb_sort([99, 15, 13, 47]) == [13, 15, 47, 99]
