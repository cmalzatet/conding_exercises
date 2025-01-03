def solution(buckets):
    
    # Initial parameters
    n_balls = buckets.count('B')
    n_spaces = buckets.count('.')
    n_buckets = len(buckets)
    
    # Edge cases
    if n_balls == 0:
        print("No balls")
        return -1
    
    if (n_buckets != (n_balls + n_spaces)):
        print("Invalid input")
        return -1
    
    if (n_balls > ((n_buckets + 1)/2)):
        print("No solution - insufficient space")
        print("n_balls: ", n_balls)
        print("max balls: ", (n_buckets + 1)/2)
        return -1
    
    # Determine ball positions
    ball_positions = [index for index,char in enumerate(buckets) if char == 'B']
    
    # Distances
    distances = [abs(ball_positions[i] - ball_positions[i+1]) for i in range(len(ball_positions)-1)]
    
    try:
        initial_pattern = distances.index(2)
    except:
        print("no initial pattern")
        
def solution_2(buckets):

    # Initial parameters
    n_balls = buckets.count('B')
    n_spaces = buckets.count('.')
    n_buckets = len(buckets)
    start_index = 0
    end_index = 0
    min_shift_val = -1
    ans_start_index = -1
    
    # Edge cases
    if n_balls == 0:
        print("No balls")
        return -1
    
    if (n_buckets != (n_balls + n_spaces)):
        print("Invalid input")
        return -1
    
    if (n_balls > ((n_buckets + 1)/2)):
        print("No solution - insufficient space")
        print("n_balls: ", n_balls)
        print("max balls: ", (n_buckets + 1)/2)
        return -1
    
    # Solution 
    end_index = 2*n_balls-2 # Window width
    min_shift_val = n_balls # Initial value for min_shift_val
    
    while (end_index < n_buckets-1):
        
        ball_correct_pos = 0
        
        for i in range(start_index, end_index+1, 2):
            if (buckets[i] == 'B'):
                ball_correct_pos += 1
        
        if (min_shift_val > n_balls - ball_correct_pos):
            min_shift_val = n_balls - ball_correct_pos
            ans_start_index = start_index
        
        start_index += 1
        end_index += 1
        
    return min_shift_val
    
        
    
ex = ".B..B.B...B."
print(solution_2(ex))