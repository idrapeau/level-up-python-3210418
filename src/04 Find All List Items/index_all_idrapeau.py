def index_all(input_list, value):
  indices = []
  current_index = []
  stack = []
  current_list = input_list
  i = 0

  while True:
    if i == len(current_list):
      if current_list == input_list:
        # Return the list of indices when the loop has reached the end of the input list
        return indices
      else:
        # Continue searching the most recently-added list in the stack
        current_list, i = stack.pop()
        # Remove the last part of the current index to reflect this
        current_index.pop()
        i += 1
        continue

    if isinstance(current_list[i], list):
      # Add the previous nested list to the stack and start searching through the next one
      stack.append([current_list, i])
      current_list = current_list[i]
      # Append the index of this list to the current index to reflect this
      current_index.append(i)
      # Reset the index
      i = 0
    else:
      # If the value is found, store the index in the list of indices
      if current_list[i] == value:
        current_index.append(i)
        indices.append(current_index.copy())
        # Remove the last number in the current index and continue searching through the nested list
        current_index.pop()
      i += 1


print(index_all([1, 2, 3, 2, 5, 6, 2], 2))

print(index_all([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2))

print(index_all([[[1, 2, 3]]], 2))

print(index_all([[[1, 2, 3, 2], 2, [1, 3]], [1, 2, 3], 2], 2))