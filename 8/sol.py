class Solution:
    def __init__(self, filename):
        with open(filename) as inp:
            rows = inp.read().splitlines()
            self.matrix = [list(map(int, row)) for row in rows]

    def no_of_visible_trees(self):
        matrix = self.matrix
        count = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.is_the_tree_highest_perpendicularly(i, j):
                    count += 1
        return count

    def is_the_tree_highest_perpendicularly(self, i, j):
        matrix = self.matrix
        height = matrix[i][j]

        # check if tree is highest from left
        for col in range(j):
            if matrix[i][col] >= height:
                break
        else:
            return True

        # check if tree is highest from right
        for col in range(j+1, len(matrix[0])):
            if matrix[i][col] >= height:
                break
        else:
            return True

        # check if tree is highest from top
        for row in range(i):
            if matrix[row][j] >= height:
                break
        else:
            return True

        # check if tree is highest from bottom
        for row in range(i+1, len(matrix)):
            if matrix[row][j] >= height:
                break
        else:
            return True

        return False

    def highest_scenic_score(self):
        matrix = self.matrix
        highest_score = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                tree_scenic_score = self.tree_scenic_score(i, j)
                highest_score = max(highest_score, tree_scenic_score)

        return highest_score

    def tree_scenic_score(self, i, j):
        matrix = self.matrix
        height = matrix[i][j]
        left = right = top = bottom = 0

        # trees visible on left
        for col in range(j-1, -1, -1):
            left += 1
            if matrix[i][col] >= height:
                break

        # trees visible on right
        for col in range(j+1, len(matrix[0])):
            right += 1
            if matrix[i][col] >= height:
                break

        # trees visible on top
        for row in range(i-1, -1, -1):
            top += 1
            if matrix[row][j] >= height:
                break

        # trees visible on bottom
        for row in range(i+1, len(matrix)):
            bottom += 1
            if matrix[row][j] >= height:
                break

        score = left * right * top * bottom
        return score


def main():
    soln = Solution("8/input.txt")

    visible_trees = soln.no_of_visible_trees()
    print("visible trees:", visible_trees)

    highest_scenic_score = soln.highest_scenic_score()
    print("highest scenic score:", highest_scenic_score)


if __name__ == "__main__":
    main()
