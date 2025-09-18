# MBPP/767
### Completion
def get_Pairs_Count(arr, n, target_sum):
    count = 0
    num_count = {}

    # Count occurrences of each number in the array
    for num in arr:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    # Iterate through the array to find pairs
    for num in arr:
        complement = target_sum - num
        if complement in num_count:
            count += num_count[complement]
            # If num and complement are the same, we need to adjust the count
            if complement == num:
                count -= 1

    # Each pair is counted twice, so divide by 2
    return count // 2

# Test the function with the provided assertion
assert get_Pairs_Count([1, 1, 1, 1], 4, 2) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_Pairs_Count([1,1,1,1],4,2) == 6
    assert get_Pairs_Count([1,5,7,-1,5],5,6) == 3
    assert get_Pairs_Count([1,-2,3],3,1) == 1
