

def list_sum_recursion(nums):
  # break condition
  if len(nums) == 1:
    return nums[0]
  else:
    return nums[0] + list_sum_recursion(nums[1:])



print(list_sum_recursion([1,3,5,7,9]))
