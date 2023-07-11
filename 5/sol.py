from collections import defaultdict

def find_topmost_crates_in_stacks():
    with open("5/input.txt") as inp:
        lines = inp.read().splitlines()
        move_start_line = 0

        stacks = defaultdict(list)

        # get the correct crates in stacks. These will be currently in reversed order 
        # because we are reading file from top to bottom
        for i, line in enumerate(lines):
            if not line:
                move_start_line = i + 1
                break
            for idx, char in enumerate(line):
                if not char.isalpha():
                    continue
                stack = ((idx - 1)//4) + 1
                stacks[stack].append(char)
        
        # reverse the order of crates in stacks
        stacks = {key:value[::-1] for key, value in stacks.items()}

        # move items between stacks
        for line in lines[move_start_line:]:
            count, from_stack, to_stack = tuple(map(int, (elem for elem in line.split(" ") if elem.isdigit())))
            for _ in range(count):
                stacks[to_stack].append(stacks[from_stack].pop())
        
        # find the top most crate in all stacks in sorted order and append it to top_crates list
        top_crates = []
        for stack in range(1, len(stacks.keys()) + 1):
            if (stacks[stack]):
                last_crate = stacks[stack].pop()
            else: 
                last_crate = " "
            top_crates.append(last_crate)
        
        # return the final answer as string
        return "".join(top_crates)

def main():
    print(find_topmost_crates_in_stacks())
    pass


if __name__ == "__main__":
    main()