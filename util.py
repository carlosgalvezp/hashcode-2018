def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def ride_distance_end_to_start(ride1, ride2):
    return distance(ride1.end, ride2.start)
