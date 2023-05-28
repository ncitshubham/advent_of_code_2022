def get_total_points():
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
    WIN_POINTS = 6
    DRAW_POINTS = 3

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


def main():
    print(get_total_points())


if __name__ == "__main__":
    main()
