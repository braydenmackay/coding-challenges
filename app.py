# Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)
# Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.

def reverse_number(n):
  if n > 0:
    n = str(n)
    reverse_str = n[::-1]
    return int(reverse_str)
  else:
    n = n * -1
    n = str(n)
    reverse_str = n[::-1]
    return int(reverse_str) * -1
