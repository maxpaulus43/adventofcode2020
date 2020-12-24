
class Seat:
    @classmethod
    def from_str(clazz, seat_string):
        converted_string = (seat_string.strip().replace("B", "1")
            .replace("F", "0")
            .replace("R", "1")
            .replace("L", "0"))

        seat = Seat()
        seat.row = int(converted_string[:-3], 2)
        seat.column = int(converted_string[-3:], 2)
        return seat

    def __init__(self) -> None:
        self.row = None
        self.column = None

    def get_seat_id(self) -> int:
        return self.row * 8 + self.column

    def __repr__(self) -> str:
        return f"\nSeat(row: {self.row}, column: {self.column}, id:{self.get_seat_id()})"
        
if __name__ == "__main__":
    with open("day_5/input.txt") as fin:
        seats = sorted([Seat.from_str(line) for line in fin], key=lambda seat: seat.get_seat_id())
        for i in range(1, len(seats)):
            if seats[i].get_seat_id() - seats[i - 1].get_seat_id() > 1:
                print(seats[i].get_seat_id() - 1)


    