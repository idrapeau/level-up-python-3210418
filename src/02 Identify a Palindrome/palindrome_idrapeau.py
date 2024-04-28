def is_palindrome(input_string):
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
  # Set the input string to lowercase
  input_string = input_string.lower()

  processed_string  = ''

  # Remove any characters that are not in the alphabet
  for i in range(len(input_string)):
    if input_string[i] in alphabet:
      processed_string = processed_string + input_string[i]

  # Check if the processed string is a palindrome
  if processed_string[::-1] == processed_string:
    return True
  else:
    return False
  
print(is_palindrome("hello world"))
print(is_palindrome("Go hang a salami - I'm a lasagna hog."))