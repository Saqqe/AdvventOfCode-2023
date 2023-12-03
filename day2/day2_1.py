import os
import re

def load_input(input_path):
  input_file = open(input_path, "r")
  return input_file.readlines()

def parse_game(game):
  game_id = game.split(" ")[1][:-1]
  matches = [m.group() for m in re.finditer(r"\d+ (red|green|blue)", game)]
  return (game_id, matches)

def is_possible_game(game, r_cubes, g_cubes, b_cubes):
  (_, matches) = parse_game(game)
  for match in matches:
    (n, color) = match.split(" ")
    if (
      (color == "red" and int(n) > r_cubes) 
      or (color == "green" and int(n) > g_cubes)
      or (color == "blue" and int(n) > b_cubes)
    ):
      return False
  return True
      
def calculate_possible_games_sum(file_lines, r_cubes, g_cubes, b_cubes):
  possible_game_ids_sum = 0
  for game in file_lines:
    (game_id, _) = parse_game(game)
    if is_possible_game(game, r_cubes, g_cubes, b_cubes):
      possible_game_ids_sum += int(game_id)
  return possible_game_ids_sum

if __name__ == "__main__":
  input_path = os.path.join(os.path.dirname(__file__), "exData.txt")
  file_lines = load_input(input_path)
  
  r_cubes = 12
  g_cubes = 13 
  b_cubes = 14

  print("Sum of the IDs of possible games:", 
        calculate_possible_games_sum(file_lines, r_cubes, g_cubes, b_cubes))
