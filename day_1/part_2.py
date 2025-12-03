import csv

current_position = 50
count = 0

csv_file = open('test_input.csv')

rows = csv.reader(csv_file)

def count_matches(n):
  return n // 100

for row in rows:
  val = row[0]
  my_list = list(val)
  direction = my_list[0]
  number = int("".join(my_list[1:]))

  initial_position = current_position

  if direction[0] == "R":
    current_position += number
  else:
    current_position -= number

  count += abs(count_matches(current_position) - count_matches(initial_position))

  if current_position % 100 == 0:
    count += 1


print(count)


# count how many numbers between N and M modulo 100 == 0
# is it func(M) - func(N)?

# n = 569
# func(n) = 5
# m = 892
# func(m) = 8

# func(m) - func(n) = 3

# start: -10
# end: 10
# distance: 20
# end - start, 10 - (-10)

# start: 10
# end: -10
# distance: 20
# end - start, -10 - 10
