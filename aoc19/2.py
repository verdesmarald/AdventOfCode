class IntcodeComputer(object):
    def __init__(self):
        self._state = [99]
        self._ip = 0

    def load(self, program):
        self._state = list(program)
        self._ip = 0

    def run(self):
        while True:
            opcode = self._state[self._ip]

            # Add
            if opcode == 1:
                src1, src2, dest = self._state[self._ip + 1 : self._ip + 4]
                self._state[dest] = self._state[src1] + self._state[src2]
                self._ip += 4

            # Mul
            elif opcode == 2:
                src1, src2, dest = self._state[self._ip + 1 : self._ip + 4]
                self._state[dest] = self._state[src1] * self._state[src2]
                self._ip += 4

            # Exit
            elif opcode == 99:
                break

            # Panic
            else:
                raise RuntimeError(f"Invalid opcode: {self._state[self._ip]}")

        return self._state[0]

    def inspect(self):
        return (self._ip, list(self._state))


def day2():
    with open('input/2.in') as f:
        prog = [int(x.strip()) for x in f.read().split(',')]

    # Part 1
    computer = IntcodeComputer()
    prog[1] = 12
    prog[2] = 2
    computer.load(prog)
    print(f"Part 1: {computer.run()}")

    # Part 2
    target = 19690720
    for noun in range(99):
        for verb in range(99):
            prog[1] = noun
            prog[2] = verb
            computer.load(prog)
            try:
                result = computer.run()
                if result == target:
                    print(f"Part 2: {100 * noun + verb}")
            except RuntimeError:
                # Skip invalid noun/verb combos
                pass


if __name__ == "__main__":
    day2()
