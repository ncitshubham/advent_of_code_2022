import string

char_priority = {
    char: idx+1 for (idx, char) in enumerate(string.ascii_letters)
}


def cal_total_priority():
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


def main():
    print(cal_total_priority())


if __name__ == "__main__":
    main()
