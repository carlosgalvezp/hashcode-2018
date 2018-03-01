import numpy as np
from util import distance

class Output(object):
    def __init__(self):
        self.vehicle_rides = []  # List of VehicleRides

    def __str__(self):
        output = ''
        for vehicle in self.vehicle_rides:
            output += '{} {}\n'.format(len(vehicle.rides), str(vehicle))

        return output

class Vehicle(object):
    def __init__(self):
        self.rides = []  # List of ints (each int is the index of the ride)
        self.time_counter = 0  # How much time vehicle spent so far
        self.position = [0,0]

        self.last_visited_index_sorted = 0

    def __str__(self):
        return ' '.join([str(x) for x in self.rides])



def create_output(input_data):
    # Remaining rides to be assigned to vehicles
    remaining_rides = np.array([True for _ in range(input_data.n_rides)])

    # Initialize vehicle rides
    vehicles = [Vehicle() for _ in range(input_data.n_vehicles)]


    while np.any(remaining_rides):
        vehicle_found_ride = [True for _ in range(len(vehicles))]

        for vehicle, vehicle_idx in enumerate(vehicles):
            # Find best ride for vehicle
            best_ride_idx = get_best_ride(remaining_rides, input_data.rides, vehicle)

            if best_ride_idx >= 0 and best_ride_idx < len(input_data.rides):
                best_ride = input_data.rides[best_ride_idx]

                # Update vehicle data
                d_vehicle_ride_start = distance(vehicle.position, best_ride.start)
                time_start = vehicle.time_counter + d_vehicle_ride_start

                vehicle.rides.append(input_data.rides[best_ride_idx].index)
                vehicle.time_counter += d_vehicle_ride_start +                 \
                                        max(0, best_ride.start - time_start) + \
                                        best_ride.distance
                vehicle.position = best_ride.end
                vehicle.last_visited_index_sorted = best_ride_idx

                # Remove ride from list
                remaining_rides[best_ride_idx] = False
            else:
                vehicle_found_ride[vehicle_idx] = False

        if not np.any(np.array(vehicle_found_ride)):
            # No vehicle found feasible ride
            break

def get_best_ride(remaining_rides, all_rides_sorted, vehicle):
    # Get index to the first ride in the future
    first_ride_in_future_idx = -1
    for i in range(vehicle.last_visited_index_sorted, len(all_rides_sorted)):
        ride = all_rides_sorted[i]

        if ride.start_time >= vehicle.time_counter:
            first_ride_in_future_idx = i
            break

    # Find best ride for vehicle at this point in time
    best_ride_idx = -1
    best_score = -1
    for i in range(first_ride_in_future_idx, min(first_ride_in_future_idx + 100, len(all_rides_sorted)-1)):
        ride_i = all_rides_sorted[i]

        score = compute_vehicle_ride_score(vehicle, ride_i, i, remaining_rides)

        if score >= best_score:
            best_ride_idx = i
            best_score = score

    return best_ride_idx


def compute_vehicle_ride_score(vehicle, ride, ride_idx_sorted, remaining_rides):
    score = 0

    d_vehicle_ride_start = distance(vehicle.position, ride.start)
    time_start = vehicle.time_counter + d_vehicle_ride_start

    if not remaining_rides[ride_idx_sorted] or not ride.is_feasible(time_start):
        score = -10
    else:
        time_waiting = max(0, ride.start - time_start)
        score = 1.0 / (d_vehicle_ride_start + time_waiting)

    return score





    r1 = Vehicle()
    r1.rides = [0]
    r2 = Vehicle()
    r2.rides = [2, 1]

    output = Output()
    output.vehicle_rides = [r1, r2]
    return output
