def mergeSort(nums):
    sort(nums, 0, len(nums) - 1)

def sort(nums, left, right):
    if left < right:
        mid = (left + right) // 2
        sort(nums, left, mid)
        sort(nums, mid + 1, right)
        merge(nums, left, mid, right)

def merge(nums, left, mid, right):
    tmp = [0 for i in range(right - left + 1)]
    p1, p2 = left, mid + 1
    p = 0
    while p1 <= mid and p2 <= right:
        if nums[p1] < nums[p2]:
            tmp[p] = nums[p1]
            p += 1
            p1 += 1
        else:
            tmp[p] = nums[p2]
            p += 1
            p2 += 1

    while p1 <= mid:
        tmp[p] = nums[p1]
        p += 1
        p1 += 1

    while p2 <= right:
        tmp[p] = nums[p2]
        p += 1
        p2 += 1

    for i in range(left, right + 1):
        nums[i] = tmp[i - left]


nums = [2,6,1,23,6,5,3]
mergeSort(nums)
print(nums)