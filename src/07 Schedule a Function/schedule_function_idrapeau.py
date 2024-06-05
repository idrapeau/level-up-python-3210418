import time

def schedule_function(event_time, function, *args):
  print(f'{function.__name__}() scheduled for {time.asctime(time.localtime(event_time))}')
  # Wait until the scheduled event time
  time.sleep(event_time - time.time())
  return function(*args)

schedule_function(time.time()+1, print, 'Howdy!')
schedule_function(time.time()+5, print, 'Seconds elapsed =', 5)
numbers = (1, 2, 3)
print(schedule_function(time.time()+3, sum, numbers))