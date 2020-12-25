from pprint import pprint as pp
from typing import List, Dict, Set, Tuple
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


def execute(i, acc, program):
    if program[i] == "":
        return -1, acc
    # END IF

    op, amount = program[i].split()
    amount = int(amount)
    program[i] = ""

    if op == "nop":
        return i+1, acc
    elif op == "acc":
        return i+1, acc + amount
    elif op == "jmp":
        return i + amount, acc
    else:
        print(f"ERROR: invalid op: {op}")
        exit(0)
    # END IF
# END execute()


def part_one():
    if (len(sys.argv) < 2):
        print("ERROR: no input file")
        exit(0)
    # END IF

    with open(sys.argv[1], "r", encoding="utf-8") as file:
        program = file.read().split("\n")
        i = 0
        acc = 0

        while True:
            i, acc = execute(i, acc, program)

            if i == -1:
                break
            # END IF
        # END WHILE

        print(acc)
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
