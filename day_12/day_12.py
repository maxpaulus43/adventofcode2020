dirs = ['N', 'E', 'S', 'W']
dir = {
    'N': (0,1),
    'E': (1,0),
    'S': (0,-1),
    'W': (-1,0)
}

class Ferry:
    def __init__(self) -> None:
        self.direction = 'E'
        self.pos = [0,0]

    def execute_instruction(self, instruction):
        action, value = instruction[0], int(instruction[1:])
        if action == 'F':
            self.pos[0] += dir[self.direction][0] * value
            self.pos[1] += dir[self.direction][1] * value
        elif action == 'L':
            turns = value / 90
            self.direction = dirs[int((dirs.index(self.direction) - turns) % 4)]
        elif action == 'R':
            turns = value / 90
            self.direction = dirs[int((dirs.index(self.direction) + turns) % 4)]
        else:
            d = dir[action]
            self.pos[0] += d[0] * value
            self.pos[1] += d[1] * value

class WaypointFerry:
    def __init__(self) -> None:
        # this is actually the delta between the waypoint and the ferry's position
        self.waypoint = [10,1]
        self.pos = [0,0]

    def execute_instruction(self, instruction):
        action, value = instruction[0], int(instruction[1:])
        if action == 'F':
            self.pos[0] += self.waypoint[0] * value
            self.pos[1] += self.waypoint[1] * value
        elif action == 'L':
            for _ in range(value // 90):
                self.waypoint[0], self.waypoint[1] = -self.waypoint[1], self.waypoint[0]
        elif action == 'R':
            for _ in range(value // 90):
                self.waypoint[0], self.waypoint[1] = self.waypoint[1], -self.waypoint[0]
        else:
            d = dir[action]
            self.waypoint[0] += d[0] * value
            self.waypoint[1] += d[1] * value

if __name__ == "__main__":
    ferry = Ferry()
    wp_ferry = WaypointFerry()
    with open("day_12/input.txt") as fin:
        for instruction in fin:
            ferry.execute_instruction(instruction)
            wp_ferry.execute_instruction(instruction)

    print(abs(ferry.pos[0]) + abs(ferry.pos[1]))
    print(abs(wp_ferry.pos[0]) + abs(wp_ferry.pos[1]))