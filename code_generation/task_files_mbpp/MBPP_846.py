# MBPP/846
### Completion
def find_platform(arrivals, departures, n):
    # Sort both the arrival and departure times
    arrivals.sort()
    departures.sort()
    
    # Initialize platform needed and result
    platform_needed = 1
    result = 1
    
    # Pointers for arrivals and departures
    i = 1  # Pointer for arrivals
    j = 0  # Pointer for departures
    
    # Process all events in sorted order
    while i < n and j < n:
        # If next event is arrival, increment platform needed
        if arrivals[i] <= departures[j]:
            platform_needed += 1
            i += 1
        # If next event is departure, decrement platform needed
        else:
            platform_needed -= 1
            j += 1
        
        # Update result if needed
        result = max(result, platform_needed)
    
    return result

# Test the function with the provided assertion
assert find_platform([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000], 6) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_platform([900, 940, 950, 1100, 1500, 1800],[910, 1200, 1120, 1130, 1900, 2000],6)==3
    assert find_platform([100,200,300,400],[700,800,900,1000],4)==4
    assert find_platform([5,6,7,8],[4,3,2,1],4)==1
