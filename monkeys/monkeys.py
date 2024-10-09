import random

TARGET = "methinks it is like a weasel"

def generate_random_string(length):
  chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
  random_str = ''
  for i in range(0, length):
    curr_char = random.choice(chars)
    random_str += curr_char

  return random_str

def score_string(str):
  correct_chars = 0
  for idx, _ in enumerate(str):
    if str[idx] == TARGET[idx]:
      correct_chars += 1

  return correct_chars / len(str)

def start_monkeys():
  curr_score = 0
  best_score = 0
  best_string = ""
  attempt_number = 0

  while curr_score < 1.0:
    random_str = generate_random_string(28)
    curr_score = score_string(random_str)

    if curr_score > best_score:
      best_score = curr_score
      best_string = random_str
      print(attempt_number, best_score, best_string)

    attempt_number += 1





start_monkeys()
