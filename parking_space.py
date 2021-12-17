import random

from empty_state import EmptyState
from disabled_state import DisabledState
from staff_state import StaffState

BASE_STATES = [EmptyState(), DisabledState(), StaffState()]
'''
Creates state objects for each empty space state, ready to be assigned to spaces as they're created.
'''


class ParkingSpace:
    def __init__(self, index):
        self.state = random.choice(BASE_STATES)
        '''
        When a space is created, a random empty space state object is created and assigned to this space object.
        This 'base state' will determine how parking requests are handled.
        '''
        self.index = index

    def park_in_space(self, car):
        """
        When the user attempts to park a car, this function will call the state specific car_parking method
        that is defined in each state's class description. In other design patterns, the logic for whether parking
        requests are accepted would be handled here with multiple if statements.
        """
        parked = self.state.car_parking(self, car)
        return parked

    def clear_space(self):
        self.state.car_leaving(self)

    def to_string(self):
        return self.state.to_string()
