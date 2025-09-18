# MBPP/578
### Completion
def interleave_lists(*lists):
    # Check if all lists are of the same length
    if not all(len(lst) == len(lists[0]) for lst in lists):
        raise ValueError("All lists must be of the same length")
    
    interleaved = []
    for i in range(len(lists[0])):
        for lst in lists:
            interleaved.append(lst[i])
    
    return interleaved

# Test the function with the provided assertion
assert interleave_lists(
    [1, 2, 3, 4, 5, 6, 7],
    [10, 20, 30, 40, 50, 60, 70],
    [100, 200, 300, 400, 500, 600, 700]
) == [1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
    assert interleave_lists([10,20],[15,2],[5,10])==[10,15,5,20,2,10]
    assert interleave_lists([11,44], [10,15], [20,5])==[11,10,20,44,15,5]
