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

        # check if tree is heighest from left
        for col in range(j):
            if matrix[i][col] >= height:
                break
        else:
            return True
        
        # check if tree is heighest from right
        for col in range(j+1, len(matrix[0])):
            if matrix[i][col] >= height:
                break
        else:
            return True

        # check if tree is heighest from top
        for row in range(i):
            if matrix[row][j] >= height:
                break
        else: 
            return True
        
        # check if tree is heighest from bottom
        for row in range(i+1,len(matrix)):
            if matrix[row][j] >= height:
                break
        else:
            return True
        
        return False

def main():
    soln = Solution("8/input.txt")
    visible_trees = soln.no_of_visible_trees()
    print("visible trees:", visible_trees)

if __name__ == "__main__":
    main()