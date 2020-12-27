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
        xmas_data = [int(line) for line in file]
        invalid_number = 167829540
        invalid_number_index = xmas_data.index(invalid_number)
        selection = xmas_data[0:invalid_number_index]
        selection_length = len(selection)
        start = 0
        end = 2
        while end <= selection_length:

            curr_start = start
            curr_end = end
            while curr_end <= selection_length:
                curr_sum = sum(selection[curr_start:curr_end])
                if curr_sum == invalid_number:
                    selection = selection[curr_start:curr_end]
                    selection.sort()
                    print(selection[0] + selection[-1])
                    return
                # END IF
                curr_start += 1
                curr_end += 1
            # END WHILE
            end += 1
        # END WHILE
    # END WITH
# END part_two()


if __name__ == "__main__":
    main()
# END IF
