import math
import sys
import time
from typing import List, Dict, Set
from collections import defaultdict


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
        count: int = 0
        answers: Set[str] = set()
        for line in file:
            line: List[str] = list(line.strip())

            if len(line) == 0:
                count += len(answers)
                answers.clear()
            else:
                answers = answers.union(set(line))
            # END IF
        # END FOR
        count += len(answers)

        print(count)
    # END WITH
# END part_one()


def part_two():
    if (len(sys.argv) < 2):
        print("ERROR: no input file")
        exit(0)
    # END IF

    with open(sys.argv[1], "r", encoding="utf-8") as file:
        count: int = 0
        answers: Set[str] = set()
        new: bool = True
        for line in file:
            line: List[str] = list(line.strip())

            if len(line) == 0:
                count += len(answers)
                answers.clear()
                new = True
            elif new:
                answers: Set[str] = answers.union(set(line))
                new = False
            else:
                answers: Set[str] = answers.intersection(set(line))
            # END IF
        # END FOR
        count += len(answers)

        print(count)
    # END WITH
# ENart_two()


if __name__ == "__main__":
    main()
# END IF
