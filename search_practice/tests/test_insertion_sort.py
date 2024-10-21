from insertion_sort import insertion_sort

class TestInsertionSort():
  def test_return_sorted_true_1(self):
    # prep
    nums = [1, 3, 2, 5, 4]
    want = [1, 2, 3, 4, 5]

    # calls
    got = insertion_sort(nums)

    # assert
    assert want == got

  def test_return_sorted_true_2(self):
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    want = [17, 20, 26, 31, 44, 54, 55, 77, 93]

    got = insertion_sort(nums)

    assert want == got
