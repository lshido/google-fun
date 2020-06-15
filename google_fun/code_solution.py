# Given ([1, 2, 3, 4], 15) return [-1, -1] or given ([4, 3, 10, 2, 8], 12) return [2, 3]
# For each element, keep adding the next values until one of three things happens:
# If the sum equals the answer, break and get the index, return the index of the current element and the end element.
# If the sum is less than the answer, keep adding the next element. 
# If the sum is more than the answer, go to the next element and repeat.
# Step 2: Check if the answer equals the value of the element.
# Step 3: If not, add the next element.
# Step 4: Check if the sum equals the answer. If it does, break and return the index of the current element, and the last summed element.
# Step 5: If it does not, check if the sum is greater than the answer.
# Step 6: If it is, continue to the next element.
# Step 7: If it is less than the answer. If it is less, keep adding the sum.
# Step 8: If you get to the last one and no answer has been found, return [-1, -1]

def solution(l, t):
    
    answer = [-1, -1]
    for x in range(len(l)):
        for y in range(1, len(l[x:])+1):
            if sum(l[x:x + y]) < t:
                continue
            elif sum(l[x:x + y]) >= t:
                break
        if sum(l[x:x + y]) > t:
            continue
        elif sum(l[x:x+y]) == t:
            answer = [x, x+y-1]
            break

    return answer