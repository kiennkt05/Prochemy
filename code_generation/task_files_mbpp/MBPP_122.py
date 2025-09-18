# MBPP/122
### Completion
import heapq

def smartNumber(n):
    if n < 1:
        return None
    
    # Initialize a min-heap
    heap = []
    # Set to keep track of unique smart numbers
    seen = set()
    
    # Start with the first smart number
    heapq.heappush(heap, 1)
    seen.add(1)
    
    # The prime factors we are interested in
    primes = [2, 3, 5]
    
    # Variable to store the current smart number
    current_smart_number = 1
    
    for _ in range(n):
        # Get the smallest smart number
        current_smart_number = heapq.heappop(heap)
        
        # Generate new smart numbers by multiplying with 2, 3, and 5
        for prime in primes:
            new_smart_number = current_smart_number * prime
            if new_smart_number not in seen:
                seen.add(new_smart_number)
                heapq.heappush(heap, new_smart_number)
    
    return current_smart_number

# Test the function
assert smartNumber(1) == 1  # The first smart number is 1
assert smartNumber(2) == 2
assert smartNumber(3) == 3
assert smartNumber(4) == 4
assert smartNumber(5) == 5
assert smartNumber(6) == 6
assert smartNumber(7) == 8
assert smartNumber(8) == 9
assert smartNumber(9) == 10
assert smartNumber(10) == 12
assert smartNumber(11) == 15
assert smartNumber(12) == 18
assert smartNumber(13) == 20
assert smartNumber(14) == 24
assert smartNumber(15) == 30

print("All tests passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert smartNumber(1) == 30
    assert smartNumber(50) == 273
    assert smartNumber(1000) == 2664
