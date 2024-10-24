from merge_two_sorted_lists import merge_two_sorted_lists

def merge_sort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]

  left = merge_sort(left)
  right = merge_sort(right)

  return merge_two_sorted_lists(left, right)
