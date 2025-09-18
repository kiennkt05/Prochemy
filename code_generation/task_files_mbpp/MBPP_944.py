# MBPP/944
### Completion
def num_position(s):
    # Initialize a list to hold the positions of numbers
    positions = []
    
    # Split the string into words
    words = s.split()
    
    # Iterate through the words and their indices
    for index, word in enumerate(words):
        # Check if the word is a digit
        if word.isdigit():
            # Print the number and its position
            print(f"Number: {word}, Position: {index}")
            # Append the position to the list
            positions.append(index)
    
    # Return the count of numbers found
    return len(positions)

# Example usage
assert num_position("there are 70 flats in this apartment") == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert num_position("there are 70 flats in this apartment")==10
    assert num_position("every adult have 32 teeth")==17
    assert num_position("isha has 79 chocolates in her bag")==9
