# MBPP/621
### Completion
import re

def increment_numerics(strings, k):
    def increment_match(match):
        # Convert the matched string to an integer, increment it, and return as string
        return str(int(match.group(0)) + k)

    # Use regex to find all numeric values in each string and increment them
    return [re.sub(r'\d+', increment_match, s) for s in strings]

# Test the function with the provided assertion
assert increment_numerics(["MSM", "234", "is", "98", "123", "best", "4"], 6) == ['MSM', '240', 'is', '104', '129', 'best', '10']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert increment_numerics(["MSM", "234", "is", "98", "123", "best", "4"] , 6) == ['MSM', '240', 'is', '104', '129', 'best', '10']
    assert increment_numerics(["Dart", "356", "is", "88", "169", "Super", "6"] , 12) == ['Dart', '368', 'is', '100', '181', 'Super', '18']
    assert increment_numerics(["Flutter", "451", "is", "44", "96", "Magnificent", "12"] , 33) == ['Flutter', '484', 'is', '77', '129', 'Magnificent', '45']
