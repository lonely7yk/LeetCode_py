from typing import List
import collections

class Solution:
    # Insert Sort: O(nlogn) 96ms 83%
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(list)
        heights = set()
        res = []

        for p in people:
            d[p[0]].append(p[1])
            heights.add(p[0])

        heights = sorted(list(heights), key=lambda x: -x)   # 逆序排序

        for height in heights:
            idxes = d[height]
            idxes.sort()
            for idx in idxes:
                res.insert(idx, [height, idx])

        return res

        
if __name__ == '__main__':
    people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

    res = Solution().reconstructQueue(people)
    print(res)