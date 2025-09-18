# MBPP/711
### Completion
def product_Equal(number):
    # Convert the number to a string to access each digit
    str_num = str(number)
    
    # Initialize products for even and odd indexed digits
    product_even = 1
    product_odd = 1
    
    # Loop through the digits and their indices
    for index, digit in enumerate(str_num):
        # Convert the character digit back to an integer
        digit_value = int(digit)
        
        # Check if the index is even or odd
        if index % 2 == 0:  # Even index
            product_even *= digit_value
        else:  # Odd index
            product_odd *= digit_value
    
    # Compare the two products
    return product_even == product_odd

# Test case
assert product_Equal(2841) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert product_Equal(2841) == True
    assert product_Equal(1234) == False
    assert product_Equal(1212) == False
