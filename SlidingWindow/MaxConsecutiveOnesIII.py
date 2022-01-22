'''
Problem Statement 
Given an array containing 0s and 1s, if you are allowed to replace no more than k 0s with 1s, find the length of the longest contiguous subarray having all 1s.
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2

Example 1:
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

Example 2:
Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
'''

def solve(arr, k):
    lPtr = rPtr = maxLen = numZerosUsed = 0
    while rPtr < len(arr):
        maxLen = max(maxLen, abs(lPtr - rPtr))
        if arr[rPtr] == 0:
            while (numZerosUsed >= k and lPtr < rPtr):
                if arr[lPtr] == 0:
                    numZerosUsed -= 1
                lPtr += 1
            numZerosUsed += 1

        rPtr += 1
        
        # Hacky fix for the 0 case.
        if arr[lPtr] == 0 and k == 0:
            lPtr += 1
    return max(maxLen, abs(lPtr - rPtr))
'''
lPtr = 0
rPtr = 0
numZerosUsed = 2
maxLen = 3
[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
             ^
                      ^
[0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1]
 ^
    ^
'''

print(solve([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
print(solve([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
print(solve([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 0))
print(solve([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 1))
print(solve([0, 0, 0, 0, 0], 0))
a = True
for i in range(0, 100):
    a = solve([0] * 100, i) == i and a
print(a)
