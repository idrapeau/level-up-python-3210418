def solve_sudoku(puzzle):
  possible_values = {}

  # Idea: Represent the black squares as lists containing the missing values for the row, column, and box
  # Initialize those lists as [0, 0, 0]
  
  # Make a dictionary of possible values for each blank space in the puzzle
  # x = row, y = column
  # If there is only one possible value for a space, update the current puzzle state with that value
  # in the corresponding space and don't add it to the dictionary
  for x in range(0, 9):
    for y in range(0, 9):
      if puzzle[x][y] == 0:
        index = (x, y)
        values_list = []

        for n in range(1, 10):
          if number_is_valid(puzzle, index, n):
            values_list.append(n)

        if len(values_list) == 1:
          puzzle[x][y] = values_list[0]
          # Update the dictionary, removing any numbers that are no longer valid
          possible_values = update_possible_values(puzzle, possible_values)
        else:
          possible_values[index] = values_list


def number_is_valid(puzzle, index, number):
  x = index[0]
  y = index[1]

  # Check if number is already in row x or if it is the missing number for the row
  for j in range(0, 9):
    if isinstance(puzzle[x][j], list):
      if puzzle[x][j][0] == number:
        return False
    elif puzzle[x][j] == number:
      return False
  
  # Check if number is already in column y or if it is the missing number for the column
  for i in range(0, 9):
    if isinstance(puzzle[i][y], list):
      if puzzle[i][y][1] == number:
        return False
    elif puzzle[i][y] == number:
      return False

  # Check if number is already in the box containing (x, y) or if it is the missing number for the box
  for i in range((x//3)*3, (x//3)*3 + 3):
    for j in range((y//3)*3, (y//3)*3 + 3):
      if isinstance(puzzle[i][j], list):
        if puzzle[i][j][2] == number:
          return False
      elif puzzle[i][j] == number:
        return False

  # Return True if number is not already in the column, row, or box containing index
  return True

# Update the dictionary, removing any numbers that are no longer valid
def update_possible_values(puzzle, possible_values):
  for key in possible_values:
      for n in possible_values[key]:
        if not number_is_valid(puzzle, key, n):
          possible_values[key].remove(n)

  return possible_values