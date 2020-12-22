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
# END main()


def part_one():
    if (len(sys.argv) < 2):
        print("ERROR: no input file")
        exit(0)
    # END IF

    with open(sys.argv[1], 'r', encoding='utf-8') as file:
        jobs: List[str] = [line.strip().split(' ') for line in file]

        valid_passwords = 0
        for job in jobs:
            range, target, password = job
            range = range.split('-')
            min: int = int(range[0])
            max: int = int(range[1])

            count = 0
            target = target[:len(target) - 1]

            for letter in password:
                if letter == target:
                    count += 1
                # END IF
            # END FOR

            if count >= min and count <= max:
                valid_passwords += 1
            # END IF
        # END FOR
        print(valid_passwords)
    # END WITH
# END part_two()


def part_two():
    if (len(sys.argv) < 2):
        print("ERROR: no input file")
        exit(0)
    # END IF

    with open(sys.argv[1], 'r', encoding='utf-8') as file:
        jobs: List[str] = [line.strip().split(' ') for line in file]

        valid_passwords = 0
        for job in jobs:
            range, target, password = job
            range = range.split('-')
            min: int = int(range[0]) - 1
            max: int = int(range[1]) - 1

            target = target[:len(target) - 1]

            if password[min] != password[max] and (password[min] == target or password[max] == target):
                valid_passwords += 1
            # END IF
        # END FOR
        print(valid_passwords)
    # END WITH
# END part_two


if __name__ == "__main__":
    main()
# END IF
