points = {
    "A": 1,
    "B": 2,
    "C": 3
}

move_map = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

win_comb = {
    "A": "C",
    "B": "A",
    "C": "B"
}
lose_comb = {
    val: key for key, val in win_comb.items()
}

strategy_map = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

WIN_POINTS = 6
DRAW_POINTS = 3


# Part 1
def get_total_points_p1():
    with open("input.txt") as inp:
        rounds = inp.read().splitlines()
        total_points = 0

        for round in rounds:
            opp_mov, my_mov = round.split(" ")
            my_mov = move_map.get(my_mov)

            total_points += points.get(my_mov)

            # if draw
            if my_mov == opp_mov:
                total_points += DRAW_POINTS
            # if win
            elif opp_mov == win_comb.get(my_mov):
                total_points += WIN_POINTS

        return total_points


# Part 2
def get_total_points_p2():
    with open("input.txt") as inp:
        rounds = inp.read().splitlines()
        total_points = 0

        for round in rounds:
            opp_mov, strategy = round.split(" ")

            total_points += strategy_map.get(strategy)

            # get my own move and add its points to total
            if strategy == "X":
                my_mov = win_comb.get(opp_mov)
            elif strategy == "Y":
                my_mov = opp_mov
            else:
                my_mov = lose_comb.get(opp_mov)

            total_points += points.get(my_mov)

        return total_points


def main():
    print(get_total_points_p2())


if __name__ == "__main__":
    main()
