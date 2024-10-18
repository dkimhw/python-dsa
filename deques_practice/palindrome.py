from deques import Deque

def is_palindrome(word):
  char_deque = Deque()
  for char in word:
    char_deque.add_rear(char)

  while not char_deque.size() > 1:
    if char_deque.remove_front() != char_deque.remove_rear():
      return False

  return True


print(is_palindrome('abba'))
print(is_palindrome("lsdkjfskf"))
print(is_palindrome("radar"))
