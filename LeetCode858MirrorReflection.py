"""
There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)

Example 1:

Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.

Note:

1 <= p <= 1000
0 <= q <= p
"""


# # Simulation
# class Solution:
#     def mirrorReflection(self, p: int, q: int) -> int:
#         cur = [q, 1]    # 第一位 q 表示纵坐标，第二位 1 表示在右边，0 表示在左边
#         inc = True
        
#         while cur[0] != 0 and cur[0] != p:
#             if inc:
#                 cur = [cur[0] + q, cur[1] ^ 1]
#                 if cur[0] > p:
#                     cur[0] = p - (cur[0] - p)
#                     inc = False
#             else:
#                 cur = [cur[0] - q, cur[1] ^ 1]
#                 if cur[0] < 0:
#                     cur[0] = -cur[0]
#                     inc = True
                    
#         if cur[0] == 0:
#             return 0
#         else:
#             if cur[1] == 1: return 1
#             else: return 2


# mathematical: O(1)
# 我们不同垂直扩展，知道 nq = mp，因此我们先要找到最小公倍数。
# 然后我们可以计算 m 和 n，如果 n 是 2 的倍数，那么说明跳了偶数次，那么一定在 2
# 如果 n 不是 2 的倍数，m 是奇数表示在上面的点，即 1，偶数表示 0
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        lcm = p * q // math.gcd(p, q)   # 算最小公倍数
        m = lcm // p                    # 算
        n = lcm // q
        
        if n % 2 == 0:
            return 2
        else:
            if m % 2 == 0:
                return 0
            else:
                return 1
