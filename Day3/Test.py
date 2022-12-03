from string import ascii_letters
scores = dict([(j, i+1)for i, j in enumerate(ascii_letters)])


with open('Day3\Input_Day3.txt', 'r') as f: 
    lines = [i.strip() for i in f.readlines()] 

    sum_priorities = 0
    for line in lines:
        a = line[:len(line)//2] # First Compartment
        b = line[len(line)//2:] # Second Compartment
        char, = set(a) & set(b) # Comparin the 2 compartments and keeping the common one as a tuple 
        sum_priorities += scores[char]
    print(f" sum of the priorities of those item types is : {sum_priorities}")

