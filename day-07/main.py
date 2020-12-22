from collections import defaultdict, deque
from pprint import pprint as pp
from typing import List, Dict, Set, Tuple
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


def check_for_gold(bags_dict: Dict[str, List[str]], bags: List[str]) -> bool:
    while len(bags) != 0:
        curr_bag = bags.pop()
        inside = bags_dict[curr_bag]
        if "shiny gold" in inside:
            return True
        else:
            bags += bags_dict[curr_bag]
        # END IF
    # END WHILE

    return False
# END check_for_gold()


def part_one():
    if (len(sys.argv) < 2):
        print("ERROR: no input file")
        exit(0)
    # END IF

    with open(sys.argv[1], "r", encoding="utf-8") as file:
        bags_dict: Dict[str, List[str]] = {}

        for line in file:
            container, bags = line.split("contain")
            container: str = container.replace("bags", "").strip()
            bags: List[str] = [bag.replace("bags", "").replace("bag", "").strip(" 0123456789")
                               for bag in bags.strip(".\n").split(",")]

            # print(container, bags)
            if bags[0] == "no other":
                bags_dict[container] = []
            else:
                bags_dict[container] = bags
            # END IF
        # END FOR

        # pp(bags_dict)

        count = 0
        for bag in bags_dict.keys():
            has_gold = check_for_gold(bags_dict, [bag])
            if has_gold == True:
                count += 1
            # END IF
        # END FOR
        print(count)
    # END WITH
# END part_one()


def part_two():
    """
    if (len(sys.argv) < 2):
        print("ERROR: no input file")
        exit(0)
    # END IF

    with open(sys.argv[1], "r", encoding="utf-8") as file:
    # END WITH
    """
# END part_two()


if __name__ == "__main__":
    main()
# END IF
