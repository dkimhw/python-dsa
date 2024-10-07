import random

def generate_random_string(length):
  chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
  random_str = ''
  for i in range(0, length):
    curr_char = random.choice(chars)
    random_str += curr_char

  return random_str


print(generate_random_string(28))
