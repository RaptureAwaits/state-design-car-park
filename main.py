"""
This program illustrates the state design pattern using a metaphorical car park consisting of spaces with particular
flags that restrict which cars can park there. The following states are used:

- EmptyState: An empty space that has no flags. Accepts all parking requests from any car.
- DisabledState: An empty space with the disabled flag. Accepts parking requests from cars with the disabled flag.
- StaffState: Same as above except for the staff flag.
- TakenState: A space will transition from one of the above states to this one when it is parked in.
                Rejects all parking requests. Will randomly revert to its original state.
- LeaveState: "Parks" the current car and progresses the program without taking up a space. Think of it as the car
                simply leaving instead of parking.

This file is largely concerned with user interaction, and has little interaction with the state classes.
"""

from parking_space import ParkingSpace
from leave_state import LeaveState

import random


class CarPark:
    def __init__(self):
        self.spaces = {}

    def construct_space_array(self):  # Creates the space objects
        size_input = None
        while size_input is None:
            try:
                user_input = int(get_user_input("Please enter a size for the car park: "))

                if user_input <= 0:
                    print("Please enter a positive integer...\n")
                else:
                    size_input = user_input
            except ValueError:
                print("Please enter a positive integer...\n")

        for i in range(0, size_input):
            self.spaces[str(i)] = ParkingSpace(i)  # Actually creates the ParkingSpace object in a list element with a random state (chosen in ParkingSpace __init__)
        self.spaces["X"] = ParkingSpace(size_input)  # Creates an additional space intended to discard the current car if it can't be parked
        self.spaces["X"].state = LeaveState()  # Sets the additional space's state to a special state that will discard the current car

    def print_space_array(self):  # Displays the states of all spaces to the user
        print("Spaces:\n")
        for key, space in self.spaces.items():
            print(f"{key}: {space.to_string()}")

    def main(self):  # Repeatedly generates cars for the user to park
        car = generate_car()

        self.print_space_array()
        print(f"\nThis car has the following flags: {car}")
        parked = False
        while not parked:
            space_input = None
            while space_input is None:
                user_input = get_user_input("Please enter a space for this car to park in: ")

                if user_input.upper() in self.spaces:
                    space_input = user_input
                else:
                    print("Please enter a valid space number...\n")

            parked = self.spaces[space_input].park_in_space(car)
            '''
            Calls the parking method in the space object, which will pass handling to the relevant method in the space's
            current state
            '''

        for space in self.spaces.values():
            space.clear_space()


CAR_PERMS = [[], ["DISABLED"], ["STAFF"], ["DISABLED", "STAFF"]]


def generate_car():  # Generates a random car for the user to park in a space
    car = random.choice(CAR_PERMS)
    return car


def get_user_input(prompt):  # Self-explanatory
    user_input = input(prompt)
    return user_input


car_park = CarPark()
car_park.construct_space_array()
while True:
    car_park.main()
