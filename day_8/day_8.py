
def parse_line(line):
    instruction, argument = line.strip().split(' ')
    return instruction, int(argument)

def run(program):
    program_counter = 0
    acc = 0
    visited = set()
    while True:
        if program_counter == len(program):
            return 0, acc

        if program_counter in visited:
            return 1, acc

        visited.add(program_counter)
        line = program[program_counter]
        
        instruction, argument = parse_line(line)
        if instruction == "acc":
            acc += argument
            program_counter += 1
        elif instruction == "jmp":
            program_counter += argument
        elif instruction == "nop":
            program_counter += 1        

if __name__ == "__main__":
    with open("day_8/input.txt") as fin:
        program = fin.readlines()
    
    for i, line in enumerate(program):
        instr, arg = parse_line(line)
        if instr == "jmp":
            new_program = list(program)
            new_program[i] = f"nop {str(arg)}"
            exit_code, acc = run(new_program)
            if exit_code == 0:
                print(acc)
                break
        elif instr == "nop":
            new_program = list(program)
            new_program[i] = f"jmp {str(arg)}"
            exit_code, acc = run(new_program)
            if exit_code == 0:
                print(acc)
                break
