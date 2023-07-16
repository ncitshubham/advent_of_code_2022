import pprint


class Solution:
    def __init__(self, input_filename):
        self.x_vals = [1]

        # create crt screen
        crt_width = 40
        crt_height = 6
        self.crt_pixels = [
            ["." for j in range(crt_width)] for i in range(crt_height)]

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

    def build_crt_screen(self):
        sprite_idx = 0

        for row in range(len(self.crt_pixels)):
            for col in range(len(self.crt_pixels[0])):
                if abs(self.x_vals[sprite_idx] - col) <= 1:
                    self.crt_pixels[row][col] = "#"
                sprite_idx += 1

    def see_crt_screen(self):
        crt_screen = ["".join(row) for row in self.crt_pixels]

        pprint.pprint(crt_screen)


def main():
    soln = Solution("10/input.txt")
    cycles = [20, 60, 100, 140, 180, 220]
    print("sum of signal strengths:", soln.sum_signal_strengths(cycles))

    soln.build_crt_screen()
    soln.see_crt_screen()


if __name__ == "__main__":
    main()
