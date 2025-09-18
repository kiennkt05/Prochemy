# MBPP/110
### Completion
def extract_missing(ranges, start, end):
    # Initialize a list to hold the missing ranges
    missing_ranges = []
    
    # Sort the ranges to ensure they are in order
    ranges.sort()
    
    # Check for missing range before the first range
    if ranges[0][0] > start:
        missing_ranges.append((start, ranges[0][0]))
    
    # Check for gaps between the provided ranges
    for i in range(len(ranges) - 1):
        current_end = ranges[i][1]
        next_start = ranges[i + 1][0]
        
        if next_start > current_end:
            missing_ranges.append((current_end, next_start))
    
    # Check for missing range after the last range
    if ranges[-1][1] < end:
        missing_ranges.append((ranges[-1][1], end))
    
    return missing_ranges

# Test the function with the provided test case
assert extract_missing([(6, 9), (15, 34), (48, 70)], 2, 100) == [(2, 6), (9, 15), (34, 48), (70, 100)]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_missing([(6, 9), (15, 34), (48, 70)], 2, 100) == [(2, 6), (9, 100), (9, 15), (34, 100), (34, 48), (70, 100)]
    assert extract_missing([(7, 2), (15, 19), (38, 50)], 5, 60) == [(5, 7), (2, 60), (2, 15), (19, 60), (19, 38), (50, 60)]
    assert extract_missing([(7, 2), (15, 19), (38, 50)], 1, 52) == [(1, 7), (2, 52), (2, 15), (19, 52), (19, 38), (50, 52)]
