import sys
import time
from typing import DefaultDict, List
from collections import defaultdict


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
        geology: List[int] = [line for line in file]

        down = 1
        down_max = len(geology)
        right = 3
        right_max = len(geology[0]) - 1
        trees_hit = 0
        while(down < down_max):
            if geology[down][right] == '#':
                trees_hit += 1
            # END IF

            down += 1
            right = (right + 3) % right_max
        # END WHILE
        print(trees_hit)
    # END WITH
# END part_two()


def part_two():
    if (len(sys.argv) < 2):
        print("ERROR: no input file")
        exit(0)
    # END IF

    with open(sys.argv[1], 'r', encoding='utf-8') as file:
        geology: List[int] = [line for line in file]
        steps: List[List[int]] = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

        down_max = len(geology)
        right_max = len(geology[0]) - 1
        result = 1
        for step in steps:
            down = step[1]
            right = step[0]
            trees_hit = 0

            while(down < down_max):
                if geology[down][right] == '#':
                    trees_hit += 1
                # END IF

                down += step[1]
                right = (right + step[0]) % right_max
            # END WHILE

            result *= trees_hit
        # END step
        print(result)
    # END WITH
# END part_two


if __name__ == "__main__":
    main()
# END IF
