
class Passport:
    @classmethod
    def from_lines(clazz, passport_lines):
        p = Passport()
        parts = [part for line in passport_lines.strip().split("\n") 
                        for part in line.strip().split(" ")]
        for part in parts:
            key, value = part.split(':')
            if key == "byr":
                p.birth_year = int(value)
            elif key == "iyr":
                p.issue_year = int(value)
            elif key == "eyr":
                p.expiration_year = int(value)
            elif key == "hgt":
                p.height = value
            elif key == "hcl":
                p.hair_color = value
            elif key == "ecl":
                p.eye_color = value
            elif key == "pid":
                p.passport_id = value
            elif key == "cid":
                p.country_id = value

        return p

    def __init__(self) -> None:
        self.birth_year = None
        self.issue_year = None
        self.expiration_year = None
        self.height = None
        self.hair_color = None
        self.eye_color = None
        self.passport_id = None
        self.country_id = None

    def is_valid(self) -> bool:
        return (self.is_birth_year_valid() and
                self.is_issue_year_valid() and
                self.is_expiration_year_valid() and
                self.is_height_valid() and
                self.is_hair_valid() and
                self.is_eye_color_valid() and
                self.is_passport_id_valid())

    def is_birth_year_valid(self) -> bool:
        return (self.birth_year is not None and
                1920 <= self.birth_year <= 2002)

    def is_issue_year_valid(self) -> bool:
        return (self.issue_year is not None and
                2010 <= self.issue_year <= 2020)

    def is_expiration_year_valid(self) -> bool:
        return (self.expiration_year is not None and
                2020 <= self.expiration_year <= 2030)

    def is_height_valid(self) -> bool:
        if self.height is None or self.height[-2:] not in ["in", "cm"]:
            return False

        h = int(self.height[:-2])
        unit = self.height[-2:]

        return ((unit == "cm" and 150 <= h <= 193) or 
                (unit == "in" and 59 <= h <= 76))

    def is_hair_valid(self) -> bool:
        return (self.hair_color is not None and 
                self.hair_color[:1] == '#' and 
                len(self.hair_color) == 7 and
                all(c in '0123456789abcdefABCDEF' for c in self.hair_color[1:]))

    def is_eye_color_valid(self) -> bool:
        return self.eye_color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def is_passport_id_valid(self) -> bool:
        return (self.passport_id is not None and 
                self.passport_id.isnumeric() and 
                len(self.passport_id) == 9)

    def __repr__(self) -> str:
        return f"\nPassport(byr:{self.birth_year}, iyr:{self.issue_year}, eyr:{self.expiration_year}, hgt:{self.height}, hcl:{self.hair_color}, ecl:{self.eye_color}, pid:{self.passport_id}, cid:{self.country_id})"

        
