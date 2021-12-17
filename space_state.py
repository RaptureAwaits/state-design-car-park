"""
This file defines the state template as an abstract class which details the methods that all states should have
"""

from abc import ABC


class SpaceState(ABC):

    def check_valid_car(self, car):
        pass

    def car_parking(self, space, car):
        pass

    def car_leaving(self, space):
        pass

    def to_string(self):
        pass
