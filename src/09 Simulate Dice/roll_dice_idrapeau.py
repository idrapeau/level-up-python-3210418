import random
import collections

def to_percentage(count, total):
  percentage = round(((count/total)*100), 2)
  return str(percentage) + "%"

def roll_dice(*args):
  iterations = 1000000
  roll_results = []

  # Roll the set of dice a number of times equal to the iterations variable
  for i in range(iterations):
    roll_total = 0
    for d in args:
      roll = random.randint(1, d)
      roll_total += roll
    roll_results.append(roll_total)
  
  # Count the number of events for each result and order them by result
  result_counts = dict(collections.Counter(roll_results))
  result_counts_ordered = collections.OrderedDict(sorted(result_counts.items()))

  # Convert the number of events for each result into a percentage
  for key in result_counts_ordered:
    result_counts_ordered[key] = to_percentage(result_counts_ordered[key], iterations)

  # Print out the results in a table
  for key in result_counts_ordered:
    print("{:<5} {:<10}".format(key, result_counts_ordered[key]))

roll_dice(6)
roll_dice(4, 6, 6)
