from collections import defaultdict
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


def check_for_gold(bags_dict: Dict[str, List[str]], known_bags: Set[str], bags: List[str], prev_bag: str) -> Tuple[bool, Set[str]]:
    curr_bag = bags.pop()

    if curr_bag in known_bags:
        if prev_bag != "":
            known_bags.add(prev_bag)
        # END IF
        return True, known_bags
    # END IF

    new_bags: List[str] = bags_dict[curr_bag]
    if len(new_bags) == 0 and len(bags) == 0:
        return False, known_bags
    elif "shiny gold" in new_bags:
        known_bags.add(curr_bag)
        return True, known_bags
    # END IF

    return check_for_gold(bags_dict, known_bags, new_bags + bags, curr_bag)
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
        known_bags = set()
        for bag in bags_dict.keys():
            has_gold, known_bags = check_for_gold(
                bags_dict, known_bags, [bag], "")
            if has_gold == True:
                known_bags.add(bag)
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
