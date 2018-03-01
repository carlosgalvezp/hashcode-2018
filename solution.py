#!/usr/bin/env python3
import sys
import os

from input import parse_input
from output import Output, VehicleRides

def process_data(data):
    print('processing data')
    return None

def produce_output(output):
    print('Hello World!')


def main():
    data = parse_input(os.path.join('/home/cgalvezd/git/hashcode-2018', 'data','b_should_be_easy.in'))
    #output = process_data(data)

    r1 = VehicleRides()
    r1.rides = [0]
    r2 = VehicleRides()
    r2.rides = [2, 1]

    output = Output()
    output.vehicle_rides = [r1, r2]
    print(output)

    #produce_output(output)

if __name__ == '__main__':
    main()
