with open('Day4\Input_Day4.txt', 'r') as f:
    f = [line.strip() for line in f.readlines()]

    # PART 1: The total number of completely overlapping assignment pairs?
    Overlap = 0
    for line in f:
        P1, P2 = line.split(',') ## splitting into pairs
        a, b = P1.split('-') ## further splitting into numbers
        c, d = P2.split('-')
        setP1, setP2 = set(range(int(a), int(b)+1)), set(range(int(c), int(d)+1)) # Using the indv numbers to generate sets for both pair
        #checking if it is a subset
        if setP1.issubset(setP2):
            Overlap += 1
        elif setP2.issubset(setP1):
            Overlap += 1
    print(f"The total number of  overlapping pair of assignments is : {Overlap}")

    # PART 2:  The total number of partial overlapping assignment pairs?
    P_Overlap = 0
    for line in f:
        P1, P2 = line.split(',') ## splitting into pairs
        a, b = P1.split('-') ## further splitting into numbers
        c, d = P2.split('-')
        setP1, setP2 = set(range(int(a), int(b)+1)), set(range(int(c), int(d)+1)) # Using the indv numbers to generate sets for both pair
        if len(setP1.intersection(setP2)) != 0:
            P_Overlap += 1
    print(f" The partial overlap of aiisgnment pairs is : {P_Overlap}")

    