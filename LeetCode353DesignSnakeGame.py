"""
Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.

Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.

When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

Example:

Given width = 3, height = 2, and food = [[1,2],[0,1]].

Snake snake = new Snake(width, height, food);

Initially the snake appears at position (0,0) and the food at (1,2).

|S| | |
| | |F|

snake.move("R"); -> Returns 0

| |S| |
| | |F|

snake.move("D"); -> Returns 0

| | | |
| |S|F|

snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )

| |F| |
| |S|S|

snake.move("U"); -> Returns 1

| |F|S|
| | |S|

snake.move("L"); -> Returns 2 (Snake eats the second food)

| |S|S|
| | |S|

snake.move("U"); -> Returns -1 (Game over because snake collides with border)
"""

from typing import List
import collections

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.x = 0  # 表示第几行
        self.y = 0  # 表示第几列
        self.occupy = collections.deque([(0, 0)]) # 用来放当前占据的位置
        self.food = collections.deque(food)

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        
        if direction == 'U': self.x -= 1
        elif direction == 'D': self.x += 1
        elif direction == 'L': self.y -= 1
        elif direction == 'R': self.y += 1
            
        # 超出边界
        if self.x < 0 or self.x >= self.height or self.y < 0 or self.y >= self.width: return -1
        
        if self.food and self.food[0] == [self.x, self.y]:  # 有食物且当前位置在食物上
            self.food.popleft()
        else:       # 没有食物的话每次都要把最早一个占据的位置移除
            self.occupy.popleft()

        if (self.x, self.y) in self.occupy: return -1   # 撞到自己
        self.occupy.append((self.x, self.y))
        
        return len(self.occupy) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
