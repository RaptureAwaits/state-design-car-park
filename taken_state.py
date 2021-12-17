from space_state import SpaceState

import random


class TakenState(SpaceState):
    def __init__(self, base_state):
        self.base_state = base_state  # Stores the space's original state so it can be reverted later

    def check_valid_car(self, car):
        pass

    def car_parking(self, space, car):
        print("This space is already occupied\n")  # Always rejects parking requests
        return False

    def car_leaving(self, space):
        is_leaving = random.choice([True, False, False, False])
        if is_leaving:
            space.state = self.base_state  # Sets the space's state to what it was before it was taken
            print(f"\nA car has left space {space.index}")

    def to_string(self):
        return f"[TAKEN] {self.base_state.identifier}"
