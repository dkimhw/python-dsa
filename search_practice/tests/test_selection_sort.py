from selection_sort import selection_sort
import pytest

test_vals = [
  ([2, 4, 5, 1, 3], [1, 2, 3, 4, 5]),
  ([54, 26, 93, 17, 77, 31, 44, 55, 20], [17, 20, 26, 31, 44, 54, 55, 77, 93])
]

@pytest.mark.parametrize("test_input,want", test_vals)
class TestSelectionSort():
  def test_selection_sort(self, test_input, want):
    selection_sort(test_input)
    assert test_input == want
