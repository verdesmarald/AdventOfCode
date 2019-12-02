def calc_required_fuel(mass, recurse):
    fuel = mass // 3 - 2

    if not recurse:
        return fuel

    total = 0
    while fuel > 0:
        total += fuel
        fuel = fuel // 3 - 2

    return total


def day1():
    # Part 1
    fuel = 0
    with open("input/1.in") as inp:
        for line in inp:
            fuel += calc_required_fuel(int(line), False)

    print(f"Part 1: {fuel}")

    # Part 2
    fuel = 0
    with open("input/1.in") as inp:
        for line in inp:
            fuel += calc_required_fuel(int(line), True)

    print(f"Part 2: {fuel}")



if __name__ == "__main__":
    day1()
