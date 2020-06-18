'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
from collections import deque
# def sliding_window_max(nums, k):
#     # Your code here
    # max_val = []
    # for i, num in enumerate(nums):
    #     window = nums[i:i + k]
    #     if len(window) == k:
    #         max_val.append(max(window))
    # return max_val

def sliding_window_max(nums, k):
    max_val = []
    de = deque()
    for i, num in enumerate(nums):
        while len(de) > 0 and num > de[-1]:
            de.pop()
        de.append(num)
        window = i - k + 1
        if window >= 0:
            max_val.append(de[0])
            if nums[window] == de[0]:
                de.popleft()
    return max_val
    
if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
     
    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
