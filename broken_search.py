def broken_search(nums, target) -> int:
    left = 0

    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        i = nums[mid]
        if i == target:
            return mid
        elif nums[left] <= i:
            if nums[left] <= target < i:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if i < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]

    assert broken_search(arr, 5) == 6
