# MBPP/584
### Completion
import re

def find_adverbs(sentence):
    # Regex pattern to find words ending with 'ly'
    pattern = r'\b(\w+ly)\b'
    
    # Find all matches along with their positions
    matches = [(match.group(0), match.start()) for match in re.finditer(pattern, sentence)]
    
    # Prepare the result in the required format
    result = []
    for adverb, start in matches:
        end = start + len(adverb) - 1  # Calculate end position
        result.append(f"{start}-{end}: {adverb}")
    
    # Join all results with a comma and return
    return ', '.join(result)

# Test case
assert find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
    assert find_adverbs("Please handle the situation carefuly") == '28-36: carefuly'
    assert find_adverbs("Complete the task quickly") == '18-25: quickly'
