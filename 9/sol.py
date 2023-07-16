import pprint


class Solution:
    def __init__(self, input_file):
        self.input_file = input_file
        matrix_size = 500
        initial_pos = matrix_size//2  # place the head and tail in the middle initially

        # Create a zero-filled matrix of size matrix size
        self.matrix = [[0 for _ in range(matrix_size)]
                       for _ in range(matrix_size)]

        # initialize the position of head and tail
        self.head_row = self.head_col = self.tail_row = self.tail_col = initial_pos

        #  mark the position as visited
        self.matrix[self.head_row][self.head_col] = 1

    def move_head(self):
        with open(self.input_file) as file:
            moves = file.read().splitlines()

            for move in moves:
                direction, steps = move.split(" ")
                steps = int(steps)

                for _ in range(steps):
                    if direction == "R":
                        self.head_col += 1
                    elif direction == "L":
                        self.head_col -= 1
                    elif direction == "U":
                        self.head_row -= 1
                    else:
                        self.head_row += 1

                    row_diff = self.head_row - self.tail_row
                    col_diff = self.head_col - self.tail_col

                    # if distance is more than 1, move tail
                    if abs(row_diff) > 1 or abs(col_diff) > 1:
                        # move tail colwise if row is same
                        if self.head_row == self.tail_row:
                            if self.head_col > self.tail_col:
                                self.tail_col += 1
                            else:
                                self.tail_col -= 1
                        # move tail rowwise if col is same
                        elif self.head_col == self.tail_col:
                            if self.head_row > self.tail_row:
                                self.tail_row += 1
                            else:
                                self.tail_row -= 1
                        # move tail diagnolly if both row and col are different
                        else:
                            if row_diff > 0:
                                self.tail_row += 1
                            else:
                                self.tail_row -= 1
                            if col_diff > 0:
                                self.tail_col += 1
                            else:
                                self.tail_col -= 1

                    # mark the tail position as visited
                    self.matrix[self.tail_row][self.tail_col] = 1

    def count_visited(self):
        count = 0
        for row in self.matrix:
            for val in row:
                count += val

        return count


def main():
    sol = Solution("9/input.txt")
    sol.move_head()
    print("visited:", sol.count_visited())


if __name__ == "__main__":
    main()
