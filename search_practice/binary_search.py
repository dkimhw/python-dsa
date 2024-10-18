
# 1. Find the midpoint
# 2. Compare the midpoint
# 3. If it's > move the idx to midpoint

def binary_search(ordered_nums, target):
  left_idx = 0
  right_idx = len(ordered_nums)

  while left_idx <= right_idx:
    midpoint = (left_idx + right_idx) // 2
    if ordered_nums[midpoint] == target:
      return True
    elif ordered_nums[midpoint] > target:
      right_idx = midpoint - 1
    else:
      left_idx = midpoint + 1

  return False
