import os
import re

def load_input(input_path):
  input_file = open(input_path, "r")
  return input_file.readlines()

def parse_game(game):
  game_id = game.split(" ")[1][:-1]
  matches = [m.group() for m in re.finditer(re_pattern, game)]
  return (game_id, matches)  

def calculate_game_power(game):
  (_, matches) = parse_game(game)
  
  min_r_cubes = 0
  min_g_cubes = 0
  min_b_cubes = 0

  for match in matches:
    (n, color) = match.split(" ")
    if color == "red" and int(n) > min_r_cubes:
      min_r_cubes = int(n)
    elif color == "green" and int(n) > min_g_cubes:
      min_g_cubes = int(n)
    elif color == "blue" and int(n) > min_b_cubes:
      min_b_cubes = int(n)

  return min_r_cubes * min_g_cubes * min_b_cubes

def calculate_total_game_power(file_lines):
  game_power_sets_sum = 0
  for game in file_lines:
    game_power_sets_sum += calculate_game_power(game)

  return game_power_sets_sum

if __name__ == "__main__":
  input_path = os.path.join(os.path.dirname(__file__), "input_p2.txt")
  file_lines = load_input(input_path)

  r_cubes = 12
  g_cubes = 13
  b_cubes = 14

  re_pattern = r"\d+ (red|green|blue)"

  print("Sum of the power games:", calculate_total_game_power(file_lines))
