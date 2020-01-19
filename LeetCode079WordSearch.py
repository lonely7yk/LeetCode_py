"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

from typing import List

class Solution:
    # DFS: 408ms 24.55%
    def exist(self, board: List[List[str]], word: str) -> bool:
        def findWordDFS(currRow, currCol, board, idx, word):
            if idx == len(word):
                return True

            # 坐标是否越界
            if currRow < 0 or currRow >= len(board) \
                or currCol < 0 or currCol >= len(board[0]): return False
            # 当前位置是否匹配 idx 位置的 word 字符
            if board[currRow][currCol] != word[idx]: return False

            board[currRow][currCol] = '.'   # 访问过的标记为 '.'

            ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for d in ds:
                if findWordDFS(currRow + d[0], currCol + d[1], board, idx + 1, word):
                    return True

            board[currRow][currCol] = word[idx] # 回溯完后改回原来的值
            return False

        if not word: return True
        if not board or not board[0]: return False

        row = len(board)
        col = len(board[0])

        for i in range(row):
            for j in range(col):
                if findWordDFS(i, j, board, 0, word):
                    return True

        return False

if __name__ == '__main__':
    board = [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    word = "ABCCED"
    # word = "SEE"
    # word = "ABCB"

    # board = [['a', 'a']]
    # word = 'aaa'

    res = Solution().exist(board, word)
    print(res)
