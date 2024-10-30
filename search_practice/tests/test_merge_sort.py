import pytest
from merge_sort import merge_sort

@pytest.mark.parametrize("unsorted_list,want", [
  ([3, 2, 12, 10, 4, 1, 5, 14, 6, 15], [1, 2, 3, 4, 5, 6, 10, 12, 14, 15]),
  ([6,11, 7, 15, 3, 14], [3, 6, 7, 11, 14, 15])
])
class TestMergeSort():
  def test_merge_sort(self, unsorted_list, want):
    # call
    merge_sort(unsorted_list)

    # assert
    assert want == unsorted_list
