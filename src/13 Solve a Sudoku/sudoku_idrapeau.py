def solve_sudoku(puzzle):
  current_puzzle = puzzle
  possible_values = {}

  # Make a dictionary of possible values for each blank space in the puzzle
  # x = row, y = column
  # If there is only one possible value for a space, update the current puzzle state with that value
  # in the corresponding space and don't add it to the dictionary
  for x in range(0, 9):
    for y in range(0, 9):
      if current_puzzle[x][y] == 0:
        index = (x, y)
        values_list = []

        for n in range(1, 10):
          if number_is_valid(current_puzzle, index, n):
            values_list.append(n)

        if len(values_list) == 1:
          current_puzzle[x][y] = values_list[0]
          # Update the dictionary, removing any numbers that are no longer valid
          possible_values = update_possible_values(current_puzzle, possible_values)
        else:
          possible_values[index] = values_list

  number_filled_in = True
  while number_filled_in:
    number_filled_in = False
    to_delete = []
    # Check for unique possible values in each row, column, and box and fill those in
    # Also check for spaces where there is only one possible value
    for key in possible_values:
      for n in possible_values[key]:
        if len(possible_values[key]) == 1:
          current_puzzle[key[0]][key[1]] = possible_values[key][0]
          possible_values[key] = []
          # Update the dictionary, removing any numbers that are no longer valid
          possible_values = update_possible_values(current_puzzle, possible_values)
          number_filled_in = True
          to_delete.append(key)
          break
        if unique_in_area(possible_values, key, n):
          current_puzzle[key[0]][key[1]] = n
          possible_values[key] = []
          # Update the dictionary, removing any numbers that are no longer valid
          possible_values = update_possible_values(current_puzzle, possible_values)
          number_filled_in = True
          to_delete.append(key)
          break

    # Delete dictionary entries corresponding to spaces that were just filled
    for key in to_delete:
      del possible_values[key]

  for row in current_puzzle:
    print(row)


def number_is_valid(puzzle, index, number):
  x = index[0]
  y = index[1]

  # Check if number is already in row x
  if number in puzzle[x]:
    return False
  
  # Check if number is already in column y
  for i in range(0, 9):
    if puzzle[i][y] == number:
      return False

  # Check if number is already in the box containing (x, y)
  for i in range((x//3)*3, (x//3)*3 + 3):
    for j in range((y//3)*3, (y//3)*3 + 3):
      if puzzle[i][j] == number:
        return False

  # Return True if number is not already in the column, row, or box containing index
  return True

# Check if a possible value is unique in its row, column, or box
def unique_in_area(possible_values, index, number):
  x = index[0]
  y = index[1]
  unique_in_row = True
  unique_in_col = True
  unique_in_box = True

  for key in possible_values:
    if key[0] == x and key[1] == y:
      continue
    if key[0] == x and number in possible_values[key]:
      unique_in_row = False
    if key[1] == y and number in possible_values[key]:
      unique_in_col = False
    if key[0]//3 == x//3 and key[1]//3 == y//3 and number in possible_values[key]:
      unique_in_box = False

  return unique_in_row or unique_in_col or unique_in_box

# Update the dictionary, removing any numbers that are no longer valid
def update_possible_values(puzzle, possible_values):
  for key in possible_values:
      for n in possible_values[key]:
        if not number_is_valid(puzzle, key, n):
          possible_values[key].remove(n)

  return possible_values

def print_sudoku(puzzle):
  horizontal_separator = "--------------------------------"
  for i in range(0, 9):
    if i%3 == 0 and i != 0:
      print(horizontal_separator)
    line = ""
    for j in range(0, 9):
      if j%3 == 0 and j != 0:
        line = line + "|  "
      if puzzle[i][j] == 0:
        line = line + "*  "
      else:
        line = line + str(puzzle[i][j]) + "  "
    print(line)
      

sample_puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                 [6, 0, 0, 1, 9, 5, 0, 0, 0],
                 [0, 9, 8, 0, 0, 0, 0, 6, 0],
                 [8, 0, 0, 0, 6, 0, 0, 0, 3],
                 [4, 0, 0, 8, 0, 3, 0, 0, 1],
                 [7, 0, 0, 0, 2, 0, 0, 0, 6],
                 [0, 6, 0, 0, 0, 0, 2, 8, 0],
                 [0, 0, 0, 4, 1, 9, 0, 0, 5],
                 [0, 0, 0, 0, 8, 0, 0, 7, 9]]

print_sudoku(sample_puzzle)

solve_sudoku(sample_puzzle)

print_sudoku(sample_puzzle)