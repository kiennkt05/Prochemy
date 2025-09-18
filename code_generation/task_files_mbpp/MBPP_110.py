# MBPP/110
### Completion
def extract_missing(ranges, start, end):
    # Sort the ranges based on the start value
    ranges.sort()
    
    # Initialize the list to hold missing ranges
    missing_ranges = []
    
    # Start checking from the given start value
    current_start = start
    
    for r in ranges:
        r_start, r_end = r
        
        # If there is a gap between current_start and the start of the current range
        if current_start < r_start:
            missing_ranges.append((current_start, r_start))
        
        # Update current_start to the end of the current range if it's greater
        current_start = max(current_start, r_end)
    
    # Check for any remaining gap after the last range up to the end value
    if current_start < end:
        missing_ranges.append((current_start, end))
    
    # Now we need to find the gaps between the ranges themselves
    for i in range(len(ranges) - 1):
        r_end = ranges[i][1]
        next_r_start = ranges[i + 1][0]
        
        if r_end < next_r_start:
            missing_ranges.append((r_end, next_r_start))
    
    return missing_ranges

# Test the function with the provided assertion
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
