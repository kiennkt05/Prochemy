# MBPP/299
### Completion
def max_aggregate(scores):
    # Dictionary to hold the aggregate scores
    aggregate_scores = {}
    
    # Iterate through each tuple in the list
    for name, score in scores:
        # If the name is already in the dictionary, add the score
        if name in aggregate_scores:
            aggregate_scores[name] += score
        else:
            # Otherwise, initialize the score for the name
            aggregate_scores[name] = score
    
    # Find the name with the maximum score
    max_name = None
    max_score = 0
    
    for name, total_score in aggregate_scores.items():
        if total_score > max_score:
            max_score = total_score
            max_name = name
    
    # Return the name with the maximum score and the score itself
    return (max_name, max_score)

# Test case
assert max_aggregate([('Juan Whelan', 90), ('Sabah Colley', 88), ('Peter Nichols', 7), 
                      ('Juan Whelan', 122), ('Sabah Colley', 84)]) == ('Juan Whelan', 212)

# Additional test cases can be added to further validate the function
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
    assert max_aggregate([('Juan Whelan',50),('Sabah Colley',48),('Peter Nichols',37),('Juan Whelan',22),('Sabah Colley',14)])==('Juan Whelan', 72)
    assert max_aggregate([('Juan Whelan',10),('Sabah Colley',20),('Peter Nichols',30),('Juan Whelan',40),('Sabah Colley',50)])==('Sabah Colley', 70)
