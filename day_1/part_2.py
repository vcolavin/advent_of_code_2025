import csv

current_position = 50
count = 0

csv_file = open('test_input.csv')

rows = csv.reader(csv_file)

def count_matches(n):
  return abs(n) // 100

def zeroes_between(start, end):
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

  zeroes = zeroes_between(start, end)

  if (end == 0):
    zeroes += 1
  elif ((end > 0 and start < 0) or (end < 0 and start > 0)):
    zeroes += 1

  count += zeroes
  print(start, end, zeroes, count)

print(count)
