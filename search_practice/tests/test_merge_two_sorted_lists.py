import pytest
from merge_two_sorted_lists import merge_two_sorted_lists

@pytest.mark.parametrize("a_list,b_list,want", [
  ([1, 2, 3, 10, 12], [4, 5, 6, 14, 15], [1, 2, 3, 4, 5, 6, 10, 12, 14, 15]),
  ([6, 7, 11], [3, 14, 15], [3, 6, 7, 11, 14, 15])
])
class TestTwoMergedSortedList():
  def test_merge_list(self, a_list, b_list, want):
    # call
    got = merge_two_sorted_lists(a_list, b_list)

    # assert
    assert got == want
