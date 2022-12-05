# parsing the stacks
def parse_Stack(input_text):
    stacks = [""] * 10
    for line in input_text[:-1]:
        for i, box in enumerate(line[1::4]):
            if box != " ":
                stacks[i+1] += box
    return stacks

input = open('Day5\Input_Day5.txt').read()
StackedCrate, RearrangementProcedure = [i.split("\n") for i in input.split("\n\n")] #splitting into stacks and rearrangement moves
stacks = parse_Stack(StackedCrate)

part1, part2 = stacks[:], stacks[:]

#looping the stacks with the moves
for moves in RearrangementProcedure:    
    _, Num_of_stacks, _, StartStack, _, EndStack = moves.split() #splitting moves into numbers
    Num_of_stacks = int(Num_of_stacks); StartStack = int(StartStack); EndStack = int(EndStack) #converting them to int

    part1[StartStack], part1[EndStack] = part1[StartStack][Num_of_stacks:], part1[StartStack][:Num_of_stacks][::-1] + part1[EndStack] #reversing the arranged stack as crates are moved one by one
    part2[StartStack], part2[EndStack] = part2[StartStack][Num_of_stacks:], part2[StartStack][:Num_of_stacks] + part2[EndStack] #modern machines takes multiple crates so need to reverse the rearrangement

print(f"the rearranged stack is : {part1[1:]}")
print("Part 1 :", "".join(a[0] for a in part1 if a))

print(f"the rearranged stack is : {part2[1:]}")
print("Part 2 :", "".join(a[0] for a in part2 if a))