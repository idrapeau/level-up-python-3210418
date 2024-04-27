def get_prime_factors(integer_input):
  prime_factors = []

  if is_prime(integer_input):
    prime_factors.append(integer_input)
  else:
    for i in range(2, integer_input//2 + 1):
      if integer_input % i == 0:
        if is_prime(i):
          prime_factors.append(i)
          prime_factors = prime_factors + get_prime_factors(integer_input//i)
          break

  return prime_factors

def is_prime(num):
  num_is_prime = True

  for i in range(2, num//2 + 1):
    if num % i == 0:
      num_is_prime = False
      break

  return num_is_prime

print(get_prime_factors(630))
print(get_prime_factors(633))
print(get_prime_factors(13))
print(get_prime_factors(2))