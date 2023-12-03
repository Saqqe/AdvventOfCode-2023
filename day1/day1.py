import re

def extract_first_and_last_digits_only(filename):
    with open(filename, 'r') as f:
        data = f.read().splitlines()

    extracted_digits = []
    for line in data:
        first_digit = re.findall(r"\d", line)[0]
        last_digit = re.findall(r"\d", line)[-1]

        extracted_digits.append((first_digit, last_digit))

    return extracted_digits

def extract_first_and_last_digits_spelled(filename):

  #open and read the file
  with open(filename, 'r') as f:
    #split lines into a list
    input_lines = f.read().splitlines()

  digits_mapping = {"one":1, "two":2, "three":3, "four":4, 
                    "five":5, "six":6, "seven":7, "eight":8, "nine":9}
  total_2 = 0

  for l in input_lines:
      in_num = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', l)
      if len(in_num[0]) > 1:
          calib_0 = digits_mapping[in_num[0]]
      else:
          calib_0 = in_num[0]
      if len(in_num[-1]) > 1:
          calib_1 = digits_mapping[in_num[-1]]
      else:
          calib_1 = in_num[-1]
      calib = int(calib_0) * 10 + int(calib_1)
      total_2 += calib
      
  return total_2



def calculate_sum_of_extracted_digits(extracted_digits):
    total_sum = 0
    for digit_pair in extracted_digits:
        first_digit = int(digit_pair[0])
        last_digit = int(digit_pair[1])

        sum_of_digits = first_digit * 10 + last_digit
        total_sum += sum_of_digits

    return total_sum


if __name__ == "__main__":
    filename = "input.txt"  # Replace with the actual filename
    #extracted_digits = extract_first_and_last_digits_spelled(filename)
    #print(extracted_digits)
    print(extract_first_and_last_digits_spelled(filename))


