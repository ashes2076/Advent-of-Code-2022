dirs = { '/':0}
cd = ['/']

with open('Day7\Input_Day7.txt', 'r') as f:
    for lines in f.readlines():
        ls = lines[:-1].split(" ")        
        if ls[0] == '$':
            if ls[1] == 'cd':
                if ls[2] == '..':
                    cd.pop()
                elif ls[2] =='/':
                    cd = ['/']
                else:
                    cd.append(ls[2])
        elif ls[0] == 'dir':
            dirs["".join(cd) + ls[1]] = 0         
        else:
            dirs["".join(cd)] += int(ls[0])           
            for i in range(1, len(cd)):
                dirs["".join(cd[:-i])] += int(ls[0])

print(f"The sum of the total size of all directories that are of size at most 10000 is : {sum( value for value in dirs.values() if value <= 100000)}")
print(f"The total of the smallest directory that , if deleted, woud free up space is : {min( value for value in dirs.values() if value >= dirs['/'] - 40000000)}")

