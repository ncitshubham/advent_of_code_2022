def count_overlapping_assgmts():
    with open("4/input.txt") as inp:
        assmts = inp.read().splitlines()

        count = 0
        for assmt in assmts:
            first, second = assmt.split(",")
            first = list(map(int, first.split("-")))
            second = list(map(int, second.split("-")))
            
            if (first[0] >= second[0] and first[1] <= second[1]) or (second[0] >= first[0] and second[1] <= first[1]):
                count += 1
            
        return count
    

def main():
    print(count_overlapping_assgmts())
    pass


if __name__ == "__main__":
    main()