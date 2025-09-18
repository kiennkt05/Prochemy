# MBPP/584
### Completion
import re

def find_adverbs(sentence):
    # Regex pattern to find adverbs ending with 'ly'
    pattern = r'\b\w+ly\b'
    
    # Find all matches in the sentence
    matches = re.finditer(pattern, sentence)
    
    # Prepare the result in the required format
    result = []
    for match in matches:
        start = match.start()
        adverb = match.group()
        result.append(f"{start}-{start + len(adverb)}: {adverb}")
    
    return ', '.join(result)

# Example usage
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
