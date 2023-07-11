def index_of_first_4_distinct_characters():
    with open("6/input.txt") as inp:
        signal = inp.readline()
        
        for i in range(len(signal)-3):
            if len(set(signal[i: i+4])) == 4:
                return i+4


def main():
    print(index_of_first_4_distinct_characters())
    pass


if __name__ == "__main__":
    main()