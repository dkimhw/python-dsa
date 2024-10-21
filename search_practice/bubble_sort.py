
"""
1. Loop through nums
2. Compare current idx with the next idx - swap if next idx element is greater
3. Keep doing this until no changes are made

"""
def bubble_sort(nums):
  # check if nothing has changed
  while True:
    num_of_swaps = 0

    for idx in range(len(nums) - 1, 0, -1):
      for jdx in range(idx):
        if nums[jdx] > nums[jdx + 1]:
          nums[jdx+1], nums[jdx] = nums[jdx], nums[jdx + 1]
          num_of_swaps += 1

    if num_of_swaps == 0:
      break

  return nums

def bubble_sort_short(a_list):
  for i in range(len(a_list) - 1, 0, -1):
    exchanges = False
    for j in range(i):
      if a_list[j] > a_list[j + 1]:
        exchanges = True
        a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
    if not exchanges:
        break
