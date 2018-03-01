from util import distance

class InputData(object):
    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.n_vehicles = 0
        self.n_rides = 0
        self.rides = []
        self.bonus = 0
        self.steps = 0

class Ride(object):
    def __init__(self):
        self.start = [0,0]
        self.end = [0,0]
        self.earliest_start = 0
        self.latest_finish = 0
        self.index = 0

        self.distance = 0
        self.max_allowed_time = 0
        self.buffer_time = 0

    def is_feasible(self, start_time):
        """Return true if the ride can be taken at the given start_time."""
        if start_time <= self.earliest_start:
            return True
        else:
            return (start_time - self.earliest_start) <= self.buffer_time

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
        input_data.n_vehicles = int(tokens[2])
        input_data.n_rides = int(tokens[3])
        input_data.bonus = int(tokens[4])
        input_data.steps = int(tokens[5])

        for i in range(input_data.n_rides):
            ride = Ride()

            tokens_ride = f.readline().split(' ')

            ride.start = [int(tokens_ride[0]), int(tokens_ride[1])]
            ride.end = [int(tokens_ride[2]), int(tokens_ride[3])]
            ride.earliest_start = int(tokens_ride[4])
            ride.latest_finish = int(tokens_ride[5])
            ride.index = i

            ride.distance = distance(ride.start, ride.end)
            ride.max_allowed_time = ride.latest_finish - ride.earliest_start
            ride.buffer_time = ride.max_allowed_time - ride.distance

            input_data.rides.append(ride)

        # Sort rides according to start time
        input_data.rides = sorted(input_data.rides, key=lambda ride: ride.latest_finish)

    return input_data
