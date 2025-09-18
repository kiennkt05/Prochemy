# MBPP/423
### Completion
def get_maxgold(mine, n, m):
    # Create a table to store the maximum gold that can be collected
    # from each cell
    gold_table = [[0 for _ in range(m)] for _ in range(n)]
    
    # Initialize the first row of the gold_table with the first row of the mine
    for j in range(m):
        gold_table[0][j] = mine[0][j]
    
    # Fill the gold_table
    for i in range(1, n):
        for j in range(m):
            # Get the maximum gold from the three possible positions
            # from where the miner can come to the current cell
            # (i, j)
            gold_from_left = gold_table[i-1][j-1] if j > 0 else 0
            gold_from_up = gold_table[i-1][j]
            gold_from_right = gold_table[i-1][j+1] if j < m - 1 else 0
            
            # Current cell gold + max of the three possible previous cells
            gold_table[i][j] = mine[i][j] + max(gold_from_left, gold_from_up, gold_from_right)
    
    # The maximum gold collected will be the maximum value in the last row
    max_gold = 0
    for j in range(m):
        max_gold = max(max_gold, gold_table[n-1][j])
    
    return max_gold

# Test the function with the provided assertion
assert get_maxgold([[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]], 4, 4) == 16
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_maxgold([[1, 3, 1, 5],[2, 2, 4, 1],[5, 0, 2, 3],[0, 6, 1, 2]],4,4)==16
    assert get_maxgold([[10,20],[30,40]],2,2)==70
    assert get_maxgold([[4,9],[3,7]],2,2)==13
