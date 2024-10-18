from binary_search_rec import binary_search_rec

class TestBinarySearchRec():
  def test_search_num_10(self):
    # prep
    nums = [1, 2, 3, 7, 8, 9, 10, 18]
    target = 10
    want = True

    # call
    got = binary_search_rec(nums, target)

    # assert
    assert want == got

  def test_search_num_21(self):
    # prep
    nums = [1, 2, 3, 7, 9, 10, 16, 18, 21, 50, 55, 60]
    target = 21
    want = True

    # call
    got = binary_search_rec(nums, target)

    # assert
    assert want == got

  def test_search_num_5(self):
    # prep
    nums = [1, 2, 3, 5, 7, 9, 10, 16, 18, 21, 50, 55, 60]
    target = 21
    want = True

    # call
    got = binary_search_rec(nums, target)

    # assert
    assert want == got

  def test_search_num_six(self):
    # prep
    nums = [1, 2, 3, 5, 7, 9, 10, 16, 18, 21, 50, 55, 60]
    target = 6
    want = False

    # call
    got = binary_search_rec(nums, target)

    # assert
    assert want == got