'''
Problem Statement 
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but once you have started you cant skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both the baskets.
Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''

def solve(fruits):
    maxLen = lPtr = rPtr = 0
    baskets = dict()

    while rPtr < len(fruits):
        fruit = fruits[rPtr]
        maxLen = max(maxLen, abs(lPtr - rPtr))
        if fruit not in baskets:
            if len(baskets.keys()) == 2:
                # Move left pointer until we have 1 fruit left.
                while (len(baskets.keys()) == 2):
                    removedFruit = fruits[lPtr]
                    baskets[removedFruit] -= 1
                    lPtr += 1

                    for fruitType in baskets.keys():
                        if baskets[fruitType] == 0:
                            del baskets[fruitType]
            baskets[fruit] = 0
        baskets[fruit] += 1
        rPtr += 1
    return max(maxLen, abs(lPtr - rPtr))

'''
maxLen = 5
lPtr = 1
rPtr = 2
baskets = {B:3, C:2}
['A', 'B', 'C', 'B', 'B', 'C']
       ^
                           ^

'''
print(solve(['A', 'B', 'C', 'B', 'B', 'C']) == 5)
print(solve(['A','A', 'B', 'C', 'C', 'B', 'A', 'A']) == 4)
print(solve(['A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A']) == len(['A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A']))
print(solve(['A', 'B', 'C', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C']) == len(['A', 'B', 'C', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C']) - 1)
print(solve(['A', 'B', 'C']))
print(solve(['A', 'B', 'C']))