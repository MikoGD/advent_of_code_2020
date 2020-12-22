def main():
    with open("input.txt", "r", encoding="utf-8") as file:
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
    for x in credentials:
        if "cid" in x and len(x.split()) == 8 and check_info(x):
            valid_passports += 1
        elif "cid" not in x and len(x.split()) == 7 and check_info(x):
            valid_passports += 1
        # END IF
    # END FOR
    print(valid_passports)
# ENDM main()


def check_info(credential):
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
            if not value[: len(value) - 2].isnumeric():
                valid = False
                break
            # END IF

            if value[len(value) - 2:] == "cm":
                value = int(value[: len(value) - 2])
                if value < 150 or value > 193:
                    valid = False
                    break
                #  END IF
                continue
            # END IF

            if value[len(value) - 2:] == "in":
                value = int(value[: len(value) - 2])
                if value < 59 or value > 76:
                    valid = False
                    break
                #  END IF
                continue
            # END IF
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
