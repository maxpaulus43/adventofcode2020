import sys
from typing import Deque
import time
from sympy.ntheory.modular import crt

def find_earliest_bus(my_earliest_departure, buses_in_service):
    earliest_bus_id = -1
    shortest_wait_time = sys.maxsize
    for b_id in buses_in_service:
        wait_time = b_id - (my_earliest_departure % b_id)
        if wait_time < shortest_wait_time:
            earliest_bus_id = b_id
            shortest_wait_time = wait_time

    return earliest_bus_id * shortest_wait_time

def find_earliest_offset_pattern(buses):
    bus_queue = Deque(int(b) for b in buses if b.isnumeric())
    lcm = 1
    for b in bus_queue:
        lcm *= b
    time_stamp = 0
    incr = bus_queue.popleft()
    offset_queue = Deque(i for i, b in enumerate(buses) if b.isnumeric() and i > 0)

    while len(bus_queue) > 0:
        if (time_stamp + offset_queue[0]) % bus_queue[0] == 0:
            offset_queue.popleft()
            incr *= bus_queue.popleft()
        time_stamp = (time_stamp + incr) % lcm

    return time_stamp

if __name__ == "__main__":
    with open("day_13/input.txt") as fin:
        fin_arr = fin.readlines()
        
    my_earliest_departure = int(fin_arr[0])
    buses = fin_arr[1].strip().split(',')
    buses_in_service = [int(b) for b in buses if b.isnumeric()]

    # part 1
    print(find_earliest_bus(my_earliest_departure, buses_in_service))
    # part 2
    start = time.time()
    print(find_earliest_offset_pattern(buses))
    print(time.time() - start)
    print(crt([7,13,59],[0,5,6]))
