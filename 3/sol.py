import string

char_priority = {
    char: idx+1 for (idx, char) in enumerate(string.ascii_letters)
}


def cal_total_priority_p1():
    with open("input.txt") as inp:
        rucksacks = inp.read().splitlines()
        total_priority = 0

        for rucksack in rucksacks:
            mid_point = len(rucksack)//2
            items_in_first_rucksack = set(rucksack[:mid_point])
            items_in_second_rucksack = set(rucksack[mid_point:])

            common_item = (items_in_first_rucksack &
                           items_in_second_rucksack).pop()

            total_priority += char_priority[common_item]

        return total_priority


def cal_total_priority_p2():
    with open("input.txt") as inp:
        rucksacks = inp.read().splitlines()
        total_priority = 0
        ELF_GROUP_SIZE = 3

        for idx in range(0, len(rucksacks), ELF_GROUP_SIZE):
            items_in_first_rucksack = set(rucksacks[idx])
            items_in_second_rucksack = set(rucksacks[idx+1])
            items_in_third_rucksack = set(rucksacks[idx+2])

            common_item = (items_in_first_rucksack &
                           items_in_second_rucksack & items_in_third_rucksack).pop()

            total_priority += char_priority[common_item]

        return total_priority


def main():
    print(cal_total_priority_p2())


if __name__ == "__main__":
    main()
