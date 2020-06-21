"""
Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it 
rains over the nth lake, the nth lake becomes full of water. If it rains over a lake which is 
full of water, there will be a flood. Your goal is to avoid the flood in any lake.

Given an integer array rains where:

rains[i] > 0 means there will be rains over the rains[i] lake.
rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
Return an array ans where:

ans.length == rains.length
ans[i] == -1 if rains[i] > 0.
ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, 
nothing changes. (see example 4)

Example 1:

Input: rains = [1,2,3,4]
Output: [-1,-1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day full lakes are [1,2,3]
After the fourth day full lakes are [1,2,3,4]
There's no day to dry any lake and there is no flood in any lake.

Example 2:

Input: rains = [1,2,0,0,2,1]
Output: [-1,-1,2,1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day, we dry lake 2. Full lakes are [1]
After the fourth day, we dry lake 1. There is no full lakes.
After the fifth day, full lakes are [2].
After the sixth day, full lakes are [1,2].
It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.

Example 3:

Input: rains = [1,2,0,1,2]
Output: []
Explanation: After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you 
choose to dry in the 3rd day, the other one will flood.

Example 4:

Input: rains = [69,0,0,0,69]
Output: [-1,69,1,1,-1]
Explanation: Any solution on one of the forms [-1,69,x,y,-1], [-1,x,69,y,-1] or [-1,x,y,69,-1] is 
acceptable where 1 <= x,y <= 10^9

Example 5:

Input: rains = [10,20,20]
Output: []
Explanation: It will rain over lake 20 two consecutive days. There is no chance to dry any lake.

Constraints:

1 <= rains.length <= 10^5
0 <= rains[i] <= 10^9
"""

from typing import List
import bisect

# # HashMap: O(n^2)  25%
# class Solution:
#     def avoidFlood(self, rains: List[int]) -> List[int]:
#         hasRained = dict()
#         dryOrder = []
#         res = []

#         for i, rain in enumerate(rains):
#             if rain == 0: continue

#             if rain not in hasRained:
#                 hasRained[rain] = i
#             else:
#                 dryOrder.append((rain, hasRained[rain], i))  # (要 dry 的地点，在第几天后 dry, 在第几天前 dry)
#                 hasRained[rain] = i

#         for i, rain in enumerate(rains):
#             if rain != 0:
#                 res.append(-1)
#             else:
#                 if not dryOrder:
#                     res.append(1)
#                     continue

#                 for j in range(len(dryOrder)):
#                     pos, after, before = dryOrder[j]

#                     # i 应该在 (after, before) 的范围内
#                     # 如果 i <= after，说明现在 pos 的地方还没有积水，则换下一个要 dry 的地方
#                     if i <= after: continue

#                     # 如果 i >= before，说明现在 pos 的地方已经积了两次水
#                     if i >= before:
#                         return []
#                     else:
#                         res.append(pos)
#                         dryOrder.pop(j)
#                         break
#                 else:
#                     # 说明所有的都满足 i <= after，也说明现在没有需要 dry 的地方，所以随便放一个值就可以
#                     res.append(1)

#         return res if not dryOrder else []

# HashMap + Binary Search: O(n^2)
# 把可以 dry 的天都放进一个 list，然后如果遇到 lake 已经 full 的情况，在 dry 的天中找 full 的天数后最近的一天用来 dry。
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        fullLakes = dict()  # key: 湖的位置，value: 天数
        dryDays = []     # 到目前位置有哪些天可以 dry
        res = []

        for i, lake in enumerate(rains):
            if lake == 0:
                dryDays.append(i)
                res.append(1)   # 随便添加一个数
            else:
                if lake in fullLakes:
                    fullDay = fullLakes[lake]
                    idx = bisect.bisect(dryDays, fullDay)
                    if idx == len(dryDays):
                        return []
                    else:
                        toDryDay = dryDays[idx]
                        res[toDryDay] = lake
                        dryDays.pop(idx)

                res.append(-1)
                fullLakes[lake] = i

        return res


# rains = [0,1,1]
# rains = [1,2,0,0,2,1]
# rains = [1,2,0,1,2]
# rains = [69,0,0,0,69]
# rains = [10,20,20]
# rains = [1,0,2,0,2,1]
rains = [1,2,0,2,3,0,1]
# rains = [2,3,0,0,3,1,0,1,0,2,2]
res = Solution().avoidFlood(rains)
print(res)
