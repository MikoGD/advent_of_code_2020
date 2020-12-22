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
            bags = [bag]
            while len(bags) != 0:
                curr_bag = bags.pop()
                inside = bags_dict[curr_bag]
                if "shiny gold" in inside:
                    count += 1
                    break
                else:
                    bags += bags_dict[curr_bag]
                # END IF
            # END WHILE
        # END FOR
        print(count)
    # END WITH
# END part_one()


def part_two():
    if (len(sys.argv) < 2):
        print("ERROR: no input file")
        exit(0)
    # END IF

    with open(sys.argv[1], "r", encoding="utf-8") as file:
        bags_dict: Dict[str, List[str]] = {}

        for line in file:
            container, bags = line.split("contain")
            container: str = container.replace("bags", "").strip()
            bags: List[str] = [bag.replace("bags", "").replace("bag", "").strip()
                               for bag in bags.strip(".\n").split(",")]

            # print(container, bags)
            if bags[0] == "no other":
                bags_dict[container] = []
            else:
                temp = []
                for bag in bags:
                    index = bag.find(" ")
                    temp.append((int(bag[:index]), bag[index + 1:]))
                # END FOR
                bags = temp
                bags_dict[container] = bags
            # END IF
        # END FOR

        # pp(bags_dict)

        count = 0
        bags = bags_dict["shiny gold"]

        while len(bags) != 0:
            curr_bag = bags.pop()

            amount, type = curr_bag
            count += amount

            for i in range(amount):
                bags += bags_dict[type]
        # END WHILE
        print(count)
    # END WITH
# END part_two()


if __name__ == "__main__":
    main()
# END IF
