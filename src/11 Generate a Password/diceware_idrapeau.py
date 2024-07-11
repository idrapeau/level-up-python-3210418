import random

def generate_passphrase(num_words):
  passphrase = ''
  word_dict = {}

  # Convert the Diceware word list to a dictionary
  wordlist = open('src/11 Generate a Password/diceware.wordlist.asc', 'r')
  # Skip the first two lines
  header1 = wordlist.readline()
  header2 = wordlist.readline()

  for line in wordlist:
    line = line.strip()
    if line == '':
      break
    columns = line.split()
    word_dict[columns[0]] = columns[1]

  wordlist.close()

  for i in range(num_words):
    # For each word, generate a code consisting of 5 random numbers between 1 and 6
    number_code = ''
    for j in range(5):
      number_code += str(random.randint(1, 6))
    
    # Select the word corresponding to the code and add it to the passphrase
    passphrase += word_dict[number_code] + ' '

  # Remove the space from the end of the passphrase
  passphrase = passphrase.strip()
  return passphrase

if __name__ == '__main__':
  print(generate_passphrase(5))