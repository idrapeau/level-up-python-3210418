import re
import collections

def count_words(text_file_path):
  word_counts = {}

  with open(text_file_path, "r") as text_file:
    for line in text_file:
      # Remove whitespace and convert the line to upper case
      current_line = line.strip().upper()
      # Split the line into a list of words
      words = current_line.split()
      for i in range(len(words)):
        # Remove anything that isn't a letter, number, apostrophe, or hyphen from the word
        words[i] = ''.join(re.findall(r"[A-Z0-9\'-]", words[i]))
        # Check if the remaining string is empty, skip if it is
        if words[i] != "":
          # Then check if the word is in the dictionary and add it if necessary
          # Increase the count for the word by 1
          if words[i] not in word_counts.keys():
            word_counts[words[i]] = 1
          else:
            word_counts[words[i]] += 1

    text_file.close()

  total_words = len(word_counts.keys())
  word_counts_ordered = collections.OrderedDict(sorted(word_counts.items(), 
                                                       key = lambda x:x[1],
                                                       reverse = True))
  word_counts_items = list(word_counts_ordered.items())

  print(f"Total Words: {total_words} \n")
  print("Top 20 Words:")
  for i in range(20):
    print("{:<10} {:<10}".format(word_counts_items[i][0], word_counts_items[i][1]))


if __name__ == '__main__':
  count_words("src/10 Count Unique Words/shakespeare.txt")