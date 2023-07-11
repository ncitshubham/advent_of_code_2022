def index_of_first_n_distinct_characters(n):
    with open("6/input.txt") as inp:
        signal = inp.readline()
        
        for i in range(len(signal)-(n-1)):
            if len(set(signal[i: i+n])) == n:
                return i+n


def main():
    print(index_of_first_n_distinct_characters(14))


if __name__ == "__main__":
    main()