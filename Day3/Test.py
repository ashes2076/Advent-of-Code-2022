from string import ascii_letters
scores = dict([(j, i+1)for i, j in enumerate(ascii_letters)])


with open('Day3\Input_Day3.txt', 'r') as f: 
    lines = [i.strip() for i in f.readlines()] 


    ## PART 1 SUM OF THE PRIORITIES OF THOSE ITEM TYPES
    sum_priorities = 0
    for line in lines:
        a = line[:len(line)//2] # First Compartment
        b = line[len(line)//2:] # Second Compartment
        char, = set(a) & set(b) # Comparing the 2 compartments and keeping the common one as a tuple 
        sum_priorities += scores[char]
    print(f"sum of the priorities of those item types is : {sum_priorities}")

    ## PART 2   SUM OF PRIORITIES BADGES GROUP OF 3
    sum_priorities = 0
    combined =  zip(lines[::3], lines[1::3], lines[2::3])
    for a, b, c in combined:
        common_item, = set(a) & set(b) & set(c)
        sum_priorities += scores[common_item]
    print(f"sum of common items is : {sum_priorities}")
