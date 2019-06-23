# Find the greatest common denominator of two numbers
# using Euclid's Algorithm

def gcd(a, b):
  while not b is 0:
    temp = a
    a = b
    b = temp % b
  return a

# try problem with a few test cases
assert gcd(20, 8) == 4
print(gcd(20, 8))
assert gcd(60, 96) == 12
print(gcd(60, 96))