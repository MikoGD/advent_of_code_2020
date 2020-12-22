import sys
import time
from typing import List


def main():
    start_time = time.time()
    part_two()
    print("---- %s seconds ---- " % (time.time() - start_time))
# END main()


def part_two():
    if (len(sys.argv) < 2):
        print("ERROR: no input file")
        exit(0)
    # END IF

    with open(sys.argv[1], 'r', encoding='utf-8') as file:
        expenses: List[int] = [int(line) for line in file]

        while(True and expenses):
            expense1: int = expenses.pop()

            for expense2 in expenses:
                if (2020 - expense1 - expense2) in expenses:
                    print(expense1 * expense2 * (2020 - (expense1 + expense2)))
                    return
                # END IF
            # END FOR
        # END FOR
    # END WITH

# END part_two


if __name__ == "__main__":
    main()
# END IF
