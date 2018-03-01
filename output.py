class Output(object):
    def __init__(self):
        self.vehicle_rides = []  # List of VehicleRides

    def __str__(self):
        output = ''
        for vehicle in self.vehicle_rides:
            output += '{} {}\n'.format(len(vehicle.rides), str(vehicle))

        return output

class VehicleRides(object):
    def __init__(self):
        self.rides = []  # List of ints

    def __str__(self):
        return ' '.join([str(x) for x in self.rides])
