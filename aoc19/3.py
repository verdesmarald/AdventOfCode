def get_points(wire):
    points = []
    pos = (0, 0)
    for move in wire:
        direction = move[0]
        magnitude = int(move[1:])
        for x in range(magnitude):
            if direction == 'L':
                pos = (pos[0] - 1, pos[1])
            elif direction == 'R':
                pos = (pos[0] + 1, pos[1])
            elif direction == 'D':
                pos = (pos[0], pos[1] - 1)
            elif direction == 'U':
                pos = (pos[0], pos[1] + 1)

            points.append(pos)

    return points

def find_intersections(wires):
    points1 = get_points(wires[0])
    points2 = get_points(wires[1])

    intersections = set(points1).intersection(set(points2))

    return intersections


def find_shortest_path(wires):
    points1 = get_points(wires[0])
    points2 = get_points(wires[1])

    intersections = set(points1).intersection(set(points2))

    result = float("inf")
    for intersection in intersections:
        result = min(result, points1.index(intersection) + points2.index(intersection) + 2)

    return result


def manhatten(point):
    return abs(point[0]) + abs(point[1])


def day3():
    with open('input/3.in') as f:
        wire1 = f.readline().strip().split(',')
        wire2 = f.readline().strip().split(',')

    intersections = find_intersections([wire1, wire2])
    print(f"Part 1: {min([manhatten(p) for p in intersections])}")
    print(f"Part2: {find_shortest_path([wire1, wire2])}")


if __name__ == "__main__":
    day3()
