class Program:
    def __init__(self) -> None:
        self.mask = "X" * 36
        self.mem = {}

    def write_value_to_mem(self, addr, value):
        masked_value = self.apply_mask_to_value(value)
        self.mem[addr] = masked_value

    def apply_mask_to_value(self, value):
        offset = 0
        for c in reversed(self.mask):
            if c.isnumeric():
                n = int(c)
                if n == 1:
                    value = value | 1 << offset
                else:
                    value = value & ~(1 << offset)
            offset += 1
        return value

if __name__ == "__main__":
    program = Program()
    with open("day_14/input.txt") as fin:
        for line in fin:
            instr, value = line.split(" = ")
            if instr == "mask":
                program.mask = value.strip()
            else:
                program.write_value_to_mem(int(instr.split("[")[1].split("]")[0]), int(value))

    print(sum(program.mem.values()))