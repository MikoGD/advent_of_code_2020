import sys
import time
from typing import List


def main():
    start_time = time.time()
    part_one()
    print("---- Part one %s seconds ---- " % (time.time() - start_time))
    start_time = time.time()
    part_two()
    print("---- Part two %s seconds ---- " % (time.time() - start_time))
# ENDM main()


def part_one():
    if (len(sys.argv) < 2):
        print("ERROR: no input file")
        exit(0)
    # END IF

    with open(sys.argv[1], 'r', encoding='utf-8') as file:
        credentials = file.read().split('\n\n')

        valid_passports = 0
        for cred in credentials:
            cred_len = len(cred.split())
            if cred_len == 8:
                valid_passports += 1
            elif cred_len == 7 and "cid" not in cred:
                valid_passports += 1
          # END IF
        # END FOR

        print(valid_passports)
    # END WITH
# END part_one()


def part_two():
    if (len(sys.argv) < 2):
        print("ERROR: no input file")
        exit(0)
    # END IF

    with open(sys.argv[1], "r", encoding="utf-8") as file:
        credentials = []
        credential = ""
        for line in file:
            if line == "\n":
                credentials.append(credential)
                credential = ""
            else:
                line = line.strip().split()
                credential += " ".join(line)
                credential += " "
            # END IF
        # END FOR

        credentials.append(credential)
    # END WITH

    valid_passports = 0
    for cred in credentials:
        cred_len = len(cred.split())
        if cred_len == 8 and check_info_old(cred):
            valid_passports += 1
        elif "cid" not in cred and cred_len == 7 and check_info_old(cred):
            valid_passports += 1
        # END IF
    # END FOR
    print(valid_passports)
# END part_two()


def check_info(credential):
    credential = credential.split()
    cred_dict = {}

    for cred in credential:
        key, value = cred.split(':')
        cred_dict[key] = value
    # END FOR

    byr = int(cred_dict["byr"]) if cred_dict["byr"] != "" else -1
    eyr = int(cred_dict["eyr"]) if cred_dict["eyr"] != "" else -1
    iyr = int(cred_dict["iyr"]) if cred_dict["iyr"] != "" else -1
    hgt = cred_dict["hgt"]
    hcl = cred_dict["hcl"]
    ecl = cred_dict["ecl"]
    pid = cred_dict["pid"]

    if byr < 1920 or byr > 2002:
        return False
    # END IF

    if eyr < 2020 or eyr > 2030:
        return False
    # END IF

    if iyr < 2010 or iyr > 2020:
        return False
    # END IF

    measurement = hgt[len(hgt) - 2:]
    hgt_value = hgt[: len(hgt) - 2]
    if measurement not in ("cm", "in") or not hgt_value.isnumeric():
        return False
    # END IF

    hgt_value = int(hgt_value)
    if measurement == "cm" and (hgt_value < 150 or hgt_value > 193):
        return False
    elif measurement == "in" and (hgt_value < 59 or hgt_value > 76):
        return False
    # END IF

    has_hash = hcl.find('#')
    has_hash = True if has_hash != -1 else False
    hcl_value = hcl[1:]
    if not has_hash or len(hcl_value) != 6:
        return False
    # END IF

    for character in hcl_value:
        char_value = ord(character)
        if (char_value < 48 or char_value > 57) and (char_value < 97 or char_value > 102):
            return False
        # END IF
    # END FOR

    if ecl not in "amb blu brn gry grn hzl oth":
        return False
    # END IF

    if not pid.isnumeric() or len(pid) != 9:
        return False
    # END IF

    return True
# END check_info()


def check_info_old(credential):
    credential = credential.split()

    valid = True
    for info in credential:
        type, value = info.split(":")
        if type in ("byr", "eyr", "iyr"):
            if not value.isnumeric():
                valid = False
                break
            # END IF
            value = int(value)
            if type == "byr" and (value < 1920 or value > 2002):
                valid = False
                break
            elif type == "eyr" and (value < 2020 or value > 2030):
                valid = False
                break
            elif type == "iyr" and (value < 2010 or value > 2020):
                valid = False
                break
            # END IF
        elif type == "hgt":
            measurement = value[len(value) - 2:]
            height = value[: len(value) - 2]
            if not height.isnumeric():
                valid = False
                break
            # END IF

            if measurement == "cm":
                value = int(value[: len(value) - 2])
                if value < 150 or value > 193:
                    valid = False
                    break
                #  END IF
                continue
            # END IF

            if measurement == "in":
                value = int(value[: len(value) - 2])
                if value < 59 or value > 76:
                    valid = False
                    break
                #  END IF
                continue
            # END IF

            valid = False
            break
        elif type == "hcl":
            if value[0] != "#" or len(value[1:]) != 6:
                valid = False
                break
            #  END IF

            for character in list(value[1:]):
                if character not in "0123456789abcdef":
                    valid = False
                    break
            # END FOR
        elif type == "ecl":
            if value not in "amb blu brn gry grn hzl oth":
                valid = False
                break
            # END IF
        elif type == "pid":
            if not value.isnumeric() or len(value) != 9:
                valid = False
                break
            # END IF
        # END IF
    # END FOR
    return valid
# END check_info()


if __name__ == "__main__":
    main()
# END IF
