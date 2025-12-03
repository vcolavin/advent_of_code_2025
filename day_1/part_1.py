import csv

current_position = 50
count = 0

csv_file = open('input.csv')

rows = csv.reader(csv_file)

for row in rows:
  val = row[0]
  my_list = list(val)
  direction = my_list[0]
  number = int("".join(my_list[1:]))

  if direction[0] == "R":
    current_position += number
  else:
    current_position -= number

  if current_position % 100 == 0:
    count += 1


print(count)
