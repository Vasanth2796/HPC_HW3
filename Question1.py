def solution(list, num): 
    a=0 
    b=0 
    '''type in your solution, find a and b in array that a+b=num'''
    # print(numbers)
    vals = {}
    for i, val in enumerate(numbers):
        if num - val in vals:
            a = num-val
            b = numbers[i]
            break
        else:
            vals[val] = i
    return a, b 
  
numbers = [0, 21, 78, 19, 90, 13] 
print(solution(numbers, 21))
print(solution(numbers, 25))
print(solution(numbers, 103))

# Time Complexity of the Code : O(n)
