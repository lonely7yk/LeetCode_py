def quickSort(nums):
    sort(nums, 0, len(nums) - 1)

def sort(nums, left, right):
    if left < right:
        mid = partition(nums, left, right)
        sort(nums, left, mid - 1)
        sort(nums, mid + 1, right)

def partition(nums, left, right):
    pl = left
    pr = right
    pivot = nums[left]

    while pl < pr:
        # 注意先变 pr
        while nums[pr] >= pivot and pl < pr: pr -= 1
        while nums[pl] <= pivot and pl < pr: pl += 1

        if pl < pr:
            nums[pl], nums[pr] = nums[pr], nums[pl]
        else:
            nums[left], nums[pr] = nums[pr], nums[left]

    return pr

nums = [2,6,2,1,23,6,5,3]
quickSort(nums)
print(nums)