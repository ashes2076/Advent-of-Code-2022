## How many total Calories is that Elf carrying?

from itertools import groupby
f = open('Day1\input1.txt', 'r')
s = f.read()

test_list = s.splitlines()
res = [list(sub) for ele, sub in groupby(test_list, key = bool) if ele]
new_list = [list(map(int, lst)) for lst in res]
n = len(new_list)

f.close()

total_elf_food = []
for i in range(0,n):
    m = len(new_list[i])
    result = 0
    for j in range(0,m):
        result = result + (new_list[i][j])
    total_elf_food.append(result)

print("total calories by that elf", max(total_elf_food))

## Find the top three Elves carrying the most Calories

reverse_sort = sorted(total_elf_food, reverse= True)

print("sum of top 3 elfs", sum(reverse_sort[0:3]))
