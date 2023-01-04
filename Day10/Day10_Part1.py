

total = 0
cycle = 1
x = 1
crt   = []
row   = ''

with open('Day10\Input_Day10.txt') as fin:
    program = fin.readlines()

# PART 1
    for instr in program:
        cycle += 1

        if instr.startswith('addx'):
            if cycle % 40 == 20:
                total += cycle * x
            cycle += 1
            x += int(instr[5:])

        if cycle % 40 == 20:
                total += cycle * x

print('Part 1:', total)