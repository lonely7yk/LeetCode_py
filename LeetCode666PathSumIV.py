"""
If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

For each integer in this list:

The hundreds digit represents the depth D of this node, 1 <= D <= 4.
The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
The units digit represents the value V of this node, 0 <= V <= 9.
Given a list of ascending three-digits integers representing a binary tree with the depth smaller than 5, you need to return 
the sum of all paths from the root towards the leaves.

It's guaranteed that the given list represents a valid connected binary tree.

Example 1:

Input: [113, 215, 221]
Output: 12
Explanation: 
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.
 
Example 2:

Input: [113, 221]
Output: 4
Explanation: 
The tree that the list represents is: 
    3
     \
      1

The path sum is (3 + 1) = 4.
"""

from typing import List


# DFS: O(n)
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        def dfs(tree, idx, curr):
            if tree[idx] == -1: return 0

            leftChild = 2 * idx
            rightChild = 2 * idx + 1
            
            if tree[leftChild] == -1 and tree[rightChild] == -1:
                return curr + tree[idx]
            
            res = 0
            if tree[leftChild] != -1: 
                res += dfs(tree, leftChild, curr + tree[idx])
            if tree[rightChild] != -1: 
                res += dfs(tree, rightChild, curr + tree[idx])

            return res
        
        tree = [-1 for i in range(32)]
        for num in nums:
            depth = num // 100
            pos = (num % 100) // 10
            val = num % 10
            
            idx = 2 ** (depth - 1) + (pos - 1)
            tree[idx] = val
            
        return dfs(tree, 1, 0)

