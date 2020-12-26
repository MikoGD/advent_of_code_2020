from pprint import pprint as pp
import math
import sys
import time


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

    with open(sys.argv[1], "r", encoding="utf-8") as file:
        xmas_data = [int(line) for line in file]
        start = 0
        pos = 25

        while pos <= len(xmas_data):
            curr_num = xmas_data[pos]
            selection = xmas_data[start:pos]

            valid = False
            for i in range(0, 25):
                difference = abs(selection[i] - curr_num)
                if difference in selection and difference != selection[i]:
                    valid = True
                    break
                # END IF
            # END FOR

            if not valid:
                print(curr_num)
                return
            # END IF

            start += 1
            pos += 1
        # END WHILE
    # END WITH
# END part_one()


def part_two():
    if (len(sys.argv) < 2):
        print("ERROR: no input file")
        exit(0)
    # END IF

    with open(sys.argv[1], "r", encoding="utf-8") as file:
        print("Part two")
    # END WITH
# END part_two()


if __name__ == "__main__":
    main()
# END IF
