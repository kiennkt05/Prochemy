# MBPP/846
### Completion
def find_platform(arrivals, departures, n):
    # Sort both arrival and departure times
    arrivals.sort()
    departures.sort()
    
    # Initialize pointers for arrivals and departures
    i = 0  # Pointer for arrivals
    j = 0  # Pointer for departures
    platforms_needed = 0  # Current platforms needed
    max_platforms = 0  # Maximum platforms needed at any time
    
    # Loop until we have processed all arrivals or departures
    while i < n and j < n:
        # If the next event is an arrival
        if arrivals[i] <= departures[j]:
            platforms_needed += 1  # Increase platform count
            i += 1  # Move to the next arrival
            max_platforms = max(max_platforms, platforms_needed)  # Update max platforms
        else:
            platforms_needed -= 1  # Decrease platform count
            j += 1  # Move to the next departure
    
    return max_platforms

# Test case
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
