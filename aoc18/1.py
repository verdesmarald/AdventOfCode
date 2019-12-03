def day1():
    data = []
    with open("input/1.in") as inp:
        for line in inp:
            data.append(int(line))

    # Part 1
    freq = sum(data)
    print(f"Part 1: {freq}")

    # Part 2
    freq = 0
    seen = set([freq])
    done = False
    while not done:
        for datum in data:
            freq += datum
            if freq in seen:
                done = True
                break
            seen.add(freq)

    print(f"Part 1: {freq}")


if __name__ == "__main__":
    day1()
