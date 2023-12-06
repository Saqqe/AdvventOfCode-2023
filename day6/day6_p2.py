def read_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    #print (lines)

    time_data = lines[0].split(':')[1].split()
    time_data= "".join(time_data)

    #print (time_data)

    distance_data = lines[1].split(':')[1].split()
    distance_data = "".join(distance_data)

    #print (distance_data)

    # time_data = list(map(int, time_data))
    # distance_data = list(map(int, distance_data))

    return int(time_data), int(distance_data)

def calculate_winning_ways(race_time, record_distance):
    winning_ways = 0

    for button_hold_time in range(race_time + 1):
        speed = button_hold_time
        distance = speed * (race_time - button_hold_time)

        if distance > record_distance:
            winning_ways += 1

    return winning_ways


race_time, record_distance = read_data('day6/input.txt')

print (type(race_time))

total_winning_ways = calculate_winning_ways(race_time, record_distance)

print(total_winning_ways)