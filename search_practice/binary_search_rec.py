

def binary_search_rec(ordered_nums, target):
  if len(ordered_nums) == 0:
    return False

  midpoint = len(ordered_nums) // 2
  saved_val = False
  if ordered_nums[midpoint] == target:
    return True
  elif ordered_nums[midpoint] > target:
    saved_val = binary_search_rec(ordered_nums[:midpoint], target)
  elif ordered_nums[midpoint] < target:
    saved_val = binary_search_rec(ordered_nums[midpoint + 1:], target)

  return saved_val

print(binary_search_rec([1, 2, 3, 4], 2))
