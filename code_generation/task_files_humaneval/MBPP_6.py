# MBPP/6
### Completion
def differ_At_One_Bit_Pos(num1, num2):
    # Perform XOR operation
    xor_result = num1 ^ num2
    
    # Check if xor_result has exactly one bit set
    # A number has exactly one bit set if it is greater than 0 and (n & (n - 1)) == 0
    return xor_result > 0 and (xor_result & (xor_result - 1)) == 0

# Test case
assert differ_At_One_Bit_Pos(13, 9) == True  # 13 (1101) and 9 (1001) differ at one bit position
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert differ_At_One_Bit_Pos(13,9) == True
    assert differ_At_One_Bit_Pos(15,8) == False
    assert differ_At_One_Bit_Pos(2,4) == False
