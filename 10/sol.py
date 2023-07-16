class Solution:
    def __init__(self, input_filename):
        self.x_vals = [1]

        with open(input_filename) as file:
            instructions = file.read().splitlines()

            for instn in instructions:
                instn = instn.split(" ")

                if instn[0] == "noop":
                    self.x_vals.append(self.x_vals[-1])
                else:
                    self.x_vals.append(self.x_vals[-1])
                    self.x_vals.append(self.x_vals[-1] + int(instn[1]))

    def sum_signal_strengths(self, arr):
        sig_str = 0

        for cycle in arr:
            sig_str += cycle * self.x_vals[cycle-1]

        return sig_str


def main():
    soln = Solution("10/input.txt")
    cycles = [20, 60, 100, 140, 180, 220]
    print("sum of signal strengths:", soln.sum_signal_strengths(cycles))


if __name__ == "__main__":
    main()
