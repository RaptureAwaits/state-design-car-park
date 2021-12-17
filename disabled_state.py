from space_state import SpaceState
from taken_state import TakenState


class DisabledState(SpaceState):
    def __init__(self):
        self.identifier = "Disabled Space"

    def check_valid_car(self, car):
        if "DISABLED" in car:
            return True
        else:
            return False

    def car_parking(self, space, car):
        is_valid = self.check_valid_car(car)
        if is_valid:
            space.state = TakenState(self)  # Sets the space's state to taken so no other parking requests are accepted
            input(f"This car has successfully parked in a {self.identifier}. Press enter to continue: ")
            return True
        else:
            print("This car cannot park here...\n")
            return False

    def car_leaving(self, space):
        pass

    def to_string(self):
        return f"[EMPTY] {self.identifier}"
