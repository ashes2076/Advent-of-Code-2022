#using structural pattern matching

from collections import defaultdict
from itertools import accumulate

dirs = defaultdict(int)
for lines in open('Day7\Input_Day7.txt'):
    match lines.split():
        #appending directories
        case '$', 'cd', '/': curr = ['/']
        case '$', 'cd', '..': curr.pop()
        case '$', 'cd', x: curr.append(x)
        #neglecting ls & dir
        case '$', 'ls': pass
        case 'dir', _: pass
        #accumalating the size per directory
        case size, _:
            for i in accumulate(curr):
                dirs[i] += int(size)

print(f"The sum of the total size of all directories that are of size at most 100000 is : {sum( value for value in dirs.values() if value <= 100000)}")
print(f"The total of the smallest directory that , if deleted, woud free up space is : {min( value for value in dirs.values() if value >= dirs['/'] - 40000000)}")