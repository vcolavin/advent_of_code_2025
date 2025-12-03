import csv

current_position = 50
count = 0

csv_file = open('test_input.csv')

rows = csv.reader(csv_file)

def count_matches(n):
  return abs(n) // 100

def mod_diff(start, end):
  return abs(count_matches(end) - count_matches(start))

end = current_position
for (index, row) in enumerate(rows):
  val = row[0]
  my_list = list(val)
  direction = my_list[0]
  number = int("".join(my_list[1:]))

  start = end

  if direction[0] == "R":
    end += number
  else:
    end -= number

  diff = mod_diff(start, end)


  print(f"{index + 1}.", end="")
  print("start", start, "end", end)

  if (end == 0):
    print("adding one for ending at zero")
    diff += 1
  elif ((abs(start) != start) != (abs(end) != end)):
    print("adding one for traversing zero")
    diff += 1

  count += diff


  print("diff", diff, "count", count)


print(count)


# how many numbers between (n and m] are divisible by 100?
#
