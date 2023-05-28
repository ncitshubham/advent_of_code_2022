import heapq as hq


def get_max_calories():
    with open("input.txt") as inp:
        elf_calories = []
        items = inp.read().splitlines()
        cur_total = 0

        for item in items:
            if item:
                cur_total += int(item)
            else:
                hq.heappush(elf_calories, -cur_total)
                cur_total = 0
        top_3_total = 0
        for i in range(3):
            top_3_total += -hq.heappop(elf_calories)

        return top_3_total


def main():
    print(get_max_calories())


if __name__ == "__main__":
    main()
