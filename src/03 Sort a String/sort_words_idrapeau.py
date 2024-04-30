def sort_words(input_string):
  # Split the string into a list of words to keep a record of the original capitalization
  word_list = input_string.split(" ")

  # Make a lowercase version of the list of words for sorting, then sort the list
  sorted_list = input_string.lower().split(" ")
  sorted_list.sort()
  
  # Restore the capitalization in any words that were not all lowercase
  for i in range(len(word_list)):
    if word_list[i] not in sorted_list:
      word_index = sorted_list.index(word_list[i].lower())
      sorted_list[word_index] = word_list[i]

  return sorted_list

print(sort_words("banana ORANGE apple"))
print(sort_words("Banana PEAR Orange apple"))
