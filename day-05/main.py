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


def binary_partition(input: str, range: List[int]) -> int:
    result: int = float((range[0] + range[1]) / 2)

    if input.pop(0) in 'FL':
        result = [range[0], math.floor(result)]
    else:
        result = [math.ceil(result), range[1]]

    if result[0] == result[1]:
        return result.pop()
    else:
        return binary_partition(input, result)
    # END IF
# END binary_partitiion()


def part_one():
    if (len(sys.argv) < 2):
        print("ERROR: no input file")
        exit(0)
    # END IF

    with open(sys.argv[1], 'r', encoding='utf-8') as file:
        seats: List[str] = [line for line in file.read().split('\n')]
        highest = 0

        for seat in seats:
            row, seatno = (seat[:7], seat[7:])
            row: int = binary_partition(list(row), [0, 127])
            seatno: int = binary_partition(list(seatno), [0, 7])
            seatid: int = row * 8 + seatno

            if seatid > highest:
                highest = seatid
            # END IF
        # END FOR
        print(highest)
    # END WITH
# END part_one()


def part_two():
    if (len(sys.argv) < 2):
        print("ERROR: no input file")
        exit(0)
    # END IF

    valid_seats: Dict[str, List[str]] = defaultdict(list)
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        seats: List[str] = [line for line in file.read().split('\n')]

        for seat in seats:
            if seat[:7] in 'FFFFFFFBBBBBBB':
                continue
            else:
                row = seat[:7]
                valid_seats[row].append(seat[7:])
            # END IF
        # ENF FOR

        possible_seats = {'LLR', 'LRL', 'LRR',
                          'RRL', 'RLR', 'RLL', 'LLL', 'RRR'}
        for key, value in valid_seats.items():
            if len(value) < 8:
                value.append('')
                value: Set(str) = set(value)
                value: Set = possible_seats.difference(value)
                row: int = binary_partition(list(key), [0, 127])
                seatno: int = binary_partition(list(value.pop()), [0, 7])
                print(row * 8 + seatno)
                return
                # END IF
            # END IF
        # FOR
    # END WITH
# END part_two()


if __name__ == "__main__":
    main()
# END IF
