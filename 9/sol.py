class Solution:
    def __init__(self, input_file, no_of_knots):
        self.input_file = input_file
        matrix_size = 500
        initial_pos = matrix_size//2  # place the head in the middle initially

        # Create a zero-filled matrix of size matrix size
        self.matrix = [[0 for _ in range(matrix_size)]
                       for _ in range(matrix_size)]

        # initialize the position of head and all knots in a list
        # for every position, we are storing the row and col position
        self.positions = [[initial_pos, initial_pos]
                          for _ in range(no_of_knots + 1)]

        # mark the position as visited
        self.matrix[initial_pos][initial_pos] = 1

    def move_head(self):
        with open(self.input_file) as file:
            moves = file.read().splitlines()

            for move in moves:
                direction, steps = move.split(" ")
                steps = int(steps)

                for _ in range(steps):

                    # move the head which is at self.positions[0]
                    if direction == "R":
                        self.positions[0][1] += 1
                    elif direction == "L":
                        self.positions[0][1] -= 1
                    elif direction == "U":
                        self.positions[0][0] -= 1
                    else:
                        self.positions[0][0] += 1

                    # loop through all knots and update their positions
                    for knot_no in range(1, len(self.positions)):
                        curr_knot = self.positions[knot_no]
                        prev_knot = self.positions[knot_no - 1]

                        row_diff = prev_knot[0] - curr_knot[0]
                        col_diff = prev_knot[1] - curr_knot[1]

                        # if distance is more than 1, move tail
                        if abs(row_diff) > 1 or abs(col_diff) > 1:
                            # move tail colwise if row is same
                            if prev_knot[0] == curr_knot[0]:
                                if prev_knot[1] > curr_knot[1]:
                                    curr_knot[1] += 1
                                else:
                                    curr_knot[1] -= 1
                            # move tail rowwise if col is same
                            elif prev_knot[1] == curr_knot[1]:
                                if prev_knot[0] > curr_knot[0]:
                                    curr_knot[0] += 1
                                else:
                                    curr_knot[0] -= 1
                            # move tail diagnolly if both row and col are different
                            else:
                                if row_diff > 0:
                                    curr_knot[0] += 1
                                else:
                                    curr_knot[0] -= 1
                                if col_diff > 0:
                                    curr_knot[1] += 1
                                else:
                                    curr_knot[1] -= 1

                    # mark the tail position as visited
                    self.matrix[self.positions[-1][0]
                                ][self.positions[-1][1]] = 1

    def count_visited(self):
        count = 0
        for row in self.matrix:
            for val in row:
                count += val

        return count


def main():
    sol = Solution("9/input.txt", 9)
    sol.move_head()
    print("visited:", sol.count_visited())


if __name__ == "__main__":
    main()
