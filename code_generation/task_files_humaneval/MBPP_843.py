# MBPP/843
### Completion
import heapq

def nth_super_ugly_number(n, primes):
    # Min-heap to store the next super ugly numbers
    heap = []
    # Set to track the unique super ugly numbers
    seen = set()
    
    # Start with the first super ugly number
    heapq.heappush(heap, 1)
    seen.add(1)
    
    # Variable to store the current super ugly number
    ugly_number = 1
    
    for _ in range(n):
        # Get the smallest super ugly number
        ugly_number = heapq.heappop(heap)
        
        # Generate new super ugly numbers by multiplying with each prime
        for prime in primes:
            new_ugly = ugly_number * prime
            if new_ugly not in seen:
                seen.add(new_ugly)
                heapq.heappush(heap, new_ugly)
    
    return ugly_number

# Test case
assert nth_super_ugly_number(12, [2, 7, 13, 19]) == 32
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert nth_super_ugly_number(12,[2,7,13,19])==32
    assert nth_super_ugly_number(10,[2,7,13,19])==26
    assert nth_super_ugly_number(100,[2,7,13,19])==5408
