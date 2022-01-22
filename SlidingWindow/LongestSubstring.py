'''
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
'''

def solve(string, k):
    '''
    Maintain a hashmap with counts.
    Lptr And Rptr -- when we hit something not in the dictionary this gives us two cases.
        Case i. We have used less than K
            - It's ok just add that in there.
        Case ii. We have used more than K
            - Not good, we will have to move left pointer and decrease the hashmap until we have reached less than K
    '''
    if (k == 0):
        return 0

    lptr = rptr = maxLen = 0
    charCounts = dict()
    while rptr < len(string):
        maxLen = max(maxLen, abs(lptr - rptr))
        if string[rptr] not in charCounts:
            while (len(charCounts.keys()) == k and lptr < rptr):
                charCounts[string[lptr]] -= 1
                if charCounts[string[lptr]] == 0:
                    del charCounts[string[lptr]]
                lptr += 1
            charCounts[string[rptr]] = 0
        charCounts[string[rptr]] += 1
        rptr += 1
    return max(maxLen, abs(lptr - rptr))

print(solve("araaarcccccci", 1))
print(solve("araaci", 1))
print(solve("araaci", 2))
print(solve("cbbebi", 3))