import math
def minmax(current_depth, node, max_turn, score, total_depth):
    if current_depth == total_depth:
        return score[node]
    
    if max_turn:
        return max(minmax(current_depth + 1, node * 2, False, score, total_depth),
                   minmax(current_depth + 1, node * 2 + 1, False, score, total_depth))
    else:
        return min(minmax(current_depth + 1, node * 2, True, score, total_depth),
                   minmax(current_depth + 1, node * 2 + 1, True, score, total_depth))
        
score = [3, 5, 2, 9, 12, 5, 23, 23]  
total_depth = math.log2(len(score))  
current_depth = 0  
node = 0           
max_turn = True    
print("The optimal value is:", minmax(current_depth, node, max_turn, score, total_depth))