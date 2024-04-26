def get_prime_factors(integer_input):
  prime_factors = []

  for i in range(2, integer_input-1):
    if integer_input % i == 0:
      if is_prime(i):
        integer_input = integer_input/i
        prime_factors.append(i)

  if len(prime_factors) == 0:
    prime_factors.append(integer_input) 

  return prime_factors

def is_prime(num):
  num_is_prime = True

  for i in range(2, num-1):
    if num % i == 0:
      num_is_prime = False
      break

  return num_is_prime