"""

Compare element from the two list - add the lower of the two
into sorted_list

increment the idx of the array from which the element was pulled

"""

def merge_two_sorted_lists(a_list, b_list):
  sorted_list = []
  a_list_len = len(a_list)
  b_list_len = len(b_list)

  j = i = 0

  while i < a_list_len and j < b_list_len:
    if a_list[i] < b_list[j]:
      sorted_list.append(a_list[i])
      i += 1
    else:
      sorted_list.append(b_list[j])
      j += 1

  while i < a_list_len:
    sorted_list.append(a_list[i])
    i += 1

  while j < b_list_len:
    sorted_list.append(b_list[j])
    j += 1

  return sorted_list
