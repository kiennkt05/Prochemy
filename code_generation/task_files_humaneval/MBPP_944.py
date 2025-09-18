# MBPP/944
### Completion
def num_position(input_string):
    # Initialize a list to hold the positions of numbers
    positions = []
    
    # Iterate through the string to find digits and their positions
    for index, char in enumerate(input_string):
        if char.isdigit():  # Check if the character is a digit
            positions.append((char, index))  # Store the digit and its position
    
    # Print the numbers and their positions
    for number, position in positions:
        print(f"Number: {number}, Position: {position}")
    
    # Return the count of numbers found
    return len(positions)

# Test the function with the provided assertion
assert num_position("there are 70 flats in this apartment") == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert num_position("there are 70 flats in this apartment")==10
    assert num_position("every adult have 32 teeth")==17
    assert num_position("isha has 79 chocolates in her bag")==9
