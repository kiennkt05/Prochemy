# MBPP/142
### Completion
def count_samepair(list1, list2, list3):
    # Create a set to store pairs from the first list
    pairs = set()
    
    # Iterate through the first list and create pairs
    for i in range(len(list1)):
        pairs.add((list1[i], list2[i]))
    
    # Count how many of these pairs are in the third list
    count = 0
    for i in range(len(list3)):
        if (list3[i], list2[i]) in pairs:
            count += 1
            
    return count

# Test the function with the provided assertion
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9]) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}


assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==4
assert count_samepair([1,2,3,4,2,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==5
