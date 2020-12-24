from passport import Passport

if __name__ == "__main__":
    with open("day_4/input.txt") as input_file:
        passports = []

        for passport_lines in input_file.read().split("\n\n"):
            passports.append(Passport.from_lines(passport_lines)) 

        valid_passport_count = len(list(filter(lambda p: p.is_valid(), passports)))
        print(valid_passport_count)


