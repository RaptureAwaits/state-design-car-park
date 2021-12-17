from space_state import SpaceState


class LeaveState(SpaceState):

    def check_valid_car(self, car):
        pass

    def car_parking(self, space, car):
        input(f"This car has left the car park. Press enter to continue: ")
        return True

    def car_leaving(self, space):
        pass

    def to_string(self):
        return "Leave the car park"
