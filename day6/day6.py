def read_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    #print (lines)

    time_data = lines[0].split(':')[1].split()
    #time_data= "".join(time_data)

    #print (time_data)

    distance_data = lines[1].split(':')[1].split()
    #distance_data = "".join(distance_data)

    #print (distance_data)

    time_data = list(map(int, time_data))
    distance_data = list(map(int, distance_data))

    return time_data, distance_data

def calculate_winning_distances(race_times, record_distances):
    winning_distances = []

    for race_time, record_distance in zip(race_times, record_distances):
        winning_distance = []

        for button_hold_time in range(race_time + 1):
            speed = button_hold_time
            distance = speed * (race_time - button_hold_time)

            if distance > record_distance:
                winning_distance.append(button_hold_time)

        winning_distances.append(winning_distance)

    return winning_distances


def count_winning_ways(winning_distances):
    winning_ways = 1

    for race_winning_distances in winning_distances:
        winning_ways *= len(race_winning_distances)

    return winning_ways

# Example usage
time, distance = read_data('day6/testData.txt')
print(f"Time: {time} seconds")
print(f"Distance: {distance} meters")


winning_distances = calculate_winning_distances(time, distance)
total_winning_ways = count_winning_ways(winning_distances)

print(total_winning_ways)
