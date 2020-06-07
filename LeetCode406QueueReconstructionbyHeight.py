from typing import List
import collections

# class Solution:
#     # Insert Sort: O(nlogn) 96ms 83%
#     def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
#         d = collections.defaultdict(list)
#         heights = set()
#         res = []

#         for p in people:
#             d[p[0]].append(p[1])
#             heights.add(p[0])

#         heights = sorted(list(heights), key=lambda x: -x)   # 逆序排序

#         for height in heights:
#             idxes = d[height]
#             idxes.sort()
#             for idx in idxes:
#                 res.insert(idx, [height, idx])

#         return res

# O(nlogn): 上述方法的简化，直接按照高度逆序排序，然后按照索引正序排序，然后按照索引一个个插入即可
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0],x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)

        return res

        
if __name__ == '__main__':
    people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

    res = Solution().reconstructQueue(people)
    print(res)