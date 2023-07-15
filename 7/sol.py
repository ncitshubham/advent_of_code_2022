class Node:
    def __init__(self, name, parent, size=0):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = []


class Solution:
    root = Node("/", None)
    small_dir_limit = 100_000
    total_size_of_small_dirs = 0
    
    def create_file_tree(self):
        with open("7/input.txt") as inp:
            lines = inp.read().splitlines()

            current = None

            for line in lines:
                elems = line.split(" ")

                if elems[0] == "$":
                    if elems[1] == "cd":
                        next_dir = elems[2]

                        if next_dir == "/":
                            current = self.root
                        elif next_dir == "..":
                            current = current.parent
                        elif isinstance(current.children, list):
                            for child in current.children:
                                if child.name == next_dir:
                                    current = child
                                    break
                else:
                    if elems[0] == "dir":
                        new_child = Node(elems[1], current)
                        current.children.append(new_child)
                    else:
                        new_child = Node(elems[1], current, int(elems[0]))
                        current.children.append(new_child)
        
        return self.root
            

    def calc_dir_sizes(self, node):
        if not node.children:
            return node.size
        
        size = 0
        for child in node.children:
            size += self.calc_dir_sizes(child)

        if size < self.small_dir_limit:
            self.total_size_of_small_dirs += size

        return size


def main():
    soln = Solution()
    soln.create_file_tree()

    soln.calc_dir_sizes(soln.root)
    print(soln.total_size_of_small_dirs)


if __name__ == "__main__":
    main()