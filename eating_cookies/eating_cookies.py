'''
Input: an integer
Returns: an integer
'''
import itertools
def eating_cookies(n):
    # cookies = []
    
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        # for i in range(n-1):
        #     cookies.append(i)
        # # print(list(itertools.permutations(cookies)))
        # return len(list(itertools.permutations(cookies)))
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
