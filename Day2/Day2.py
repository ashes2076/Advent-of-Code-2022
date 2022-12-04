import pandas as pd
def read_file(file_name):
    with open(file_name, 'r') as data:
        Opponent = []
        Me = []
        for line in data:
                p = line.split()
                Opponent.append(p[0])
                Me.append(p[1])
    return Opponent, Me

Opponent, Me = read_file('Day2\day2_input.txt')

#converting char to letters for opponent and me lists
for i in range(len(Opponent)):
    if Opponent[i] == 'A':
        Opponent[i] = 1
    if Opponent[i] == 'B':
        Opponent[i] = 2
    if Opponent[i] == 'C':
        Opponent[i] = 3

for i in range(len(Me)):
    if Me[i] == 'X':
        Me[i] = 1
    if Me[i] == 'Y':
        Me[i] = 2
    if Me[i] == 'Z':
        Me[i] = 3
#to be finished