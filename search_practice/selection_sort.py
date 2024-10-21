
def selection_sort(nums):
  for idx in range(len(nums) - 1, 0, -1):
    largest_val_idx = idx
    for jdx in range(0, idx):
      curr_val = nums[jdx]
      if curr_val > nums[largest_val_idx]:
        largest_val_idx = jdx

    # swap if different
    if idx != largest_val_idx:
      nums[largest_val_idx], nums[idx] = nums[idx], nums[largest_val_idx]

  return


def selection_sort_min_idx(a_list):
  for i, item in enumerate(a_list):
    min_idx = len(a_list) - 1
    for j in range(i, len(a_list)):
      if a_list[j] < a_list[min_idx]:
          min_idx = j
    if min_idx != i:
        a_list[min_idx], a_list[i] = a_list[i], a_list[min_idx]
