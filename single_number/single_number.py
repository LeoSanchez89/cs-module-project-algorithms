'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

# def single_number(arr):
#     # Your code here 
#     dupes = []
#     for i in range(len(arr)): 
#         for x in range(i+1, len(arr)): 
#             if arr[i] == arr[x] and arr[i] not in dupes: 
#                 dupes.append(arr[i]) 
#     for num in arr:
#         if num not in dupes:
#             return num 


def single_number(arr):
    counts = {}
    for num in arr:
        if num in counts:
            del counts[num]
        else:
            counts[num] = 1

    for k, v in counts.items():
        if v == 1:
            return k

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is: {single_number(arr)}")
