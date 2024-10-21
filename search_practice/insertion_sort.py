
def insertion_sort(nums):
  for i in range(len(nums)):
    cur_val = nums[i]
    cur_pos = i

    # loop backwards from j to 0
    while cur_pos > 0 and cur_val < nums[cur_pos - 1]:
      print(i, cur_pos, cur_pos - 1)
      nums[cur_pos] = nums[cur_pos - 1]
      cur_pos = cur_pos - 1

    nums[cur_pos] = cur_val
  return nums
