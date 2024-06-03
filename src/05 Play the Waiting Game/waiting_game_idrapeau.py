import random
import time

def waiting_game():
  # Return a random duration of time between 2 and 4 seconds
  target_time = random.randint(2, 4)

  print(f"Your target time is {target_time} seconds.")
  input("---Press Enter to Begin---")
  start = time.perf_counter()
  input(f"...Press Enter again after {target_time} seconds...")
  finish = time.perf_counter()

  # Round the elapsed time to 3 decimal places
  elapsed_time = round(finish - start, 3)

  print(f"Elapsed time: {elapsed_time} seconds")
  
  if elapsed_time < target_time:
    print(f"({target_time - elapsed_time:0.3f} seconds too fast)")
  elif elapsed_time > target_time:
    print(f"({elapsed_time - target_time:0.3f} seconds too slow)")
  else:
    print("(Right on target)")

waiting_game()