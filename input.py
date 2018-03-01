from util import distance

class InputData(object):
    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.vehicles = 0
        self.rides = []
        self.bonus = 0
        self.steps = 0

class Ride(object):
    def __init__(self):
        self.start = [0,0]
        self.end = [0,0]
        self.earliest_start = 0
        self.latest_finish = 0

        self.distance = distance(self.start, self.end)
        self.max_allowed_time = self.latest_finish - self.earliest_start

# Vehicle drives one unit per step
# vehicle can start new ride in the same step as previous ride finished,
# if ride starts in the same intersection as previous ride finished
def parse_input(input_file):
    input_data = InputData()

    with open(input_file, 'r') as f:
        first_line = f.readline()
        tokens = first_line.split(' ')

        input_data.rows = int(tokens[0])
        input_data.cols = int(tokens[1])
        input_data.vehicles = int(tokens[2])
        n_rides = int(tokens[3])
        input_data.bonus = int(tokens[4])
        input_data.steps = int(tokens[5])

        for _ in range(n_rides):
            ride = Ride()

            tokens_ride = f.readline().split(' ')

            ride.start = [int(tokens_ride[0]), int(tokens_ride[1])]
            ride.end = [int(tokens_ride[2]), int(tokens_ride[3])]
            ride.earliest_start = int(tokens_ride[4])
            ride.latest_finish = int(tokens_ride[5])

            input_data.rides.append(ride)

    return input_data
