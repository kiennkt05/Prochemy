# MBPP/39
### Completion
import heapq
from collections import Counter

def rearrange_string(s: str) -> str:
    # Count the frequency of each character
    char_count = Counter(s)
    
    # Create a max heap based on character frequency
    max_heap = [(-count, char) for char, count in char_count.items()]
    heapq.heapify(max_heap)
    
    result = []
    prev_char = None
    prev_count = 0
    
    while max_heap:
        count, char = heapq.heappop(max_heap)
        result.append(char)
        
        # If there was a previous character, push it back to the heap
        if prev_count < 0:
            heapq.heappush(max_heap, (prev_count, prev_char))
        
        # Update the previous character and its count
        prev_char = char
        prev_count = count + 1  # Decrease the count since we used this character
    
    rearranged = ''.join(result)
    
    # Check if the rearranged string is valid
    if len(rearranged) != len(s):
        return ""  # Not possible to rearrange
    
    return rearranged

# Test the function with the provided assertion
assert rearrange_string("aab") == 'aba'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert rearange_string("aab")==('aba')
    assert rearange_string("aabb")==('abab')
    assert rearange_string("abccdd")==('cdabcd')
