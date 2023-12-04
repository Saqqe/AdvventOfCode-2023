from collections import defaultdict

input_data = open("day4/testData.txt", "r").read().strip()
lines = input_data.split('\n')

part1_points = 0
number_counts = defaultdict(int)

for index, line in enumerate(lines):
  number_counts[index] += 1
  
  first, rest = line.split('|')
  id_, card = first.split(':')
  
  card_numbers = [int(x) for x in card.split()] 
  rest_numbers = [int(x) for x in rest.split()]
  
  matching_count = len(set(card_numbers) & set(rest_numbers))
  
  if matching_count > 0:
    part1_points += 2**(matching_count-1)

  for offset in range(matching_count):
    number_counts[index + 1 + offset] += number_counts[index]

print(part1_points)
print(sum(number_counts.values()))
