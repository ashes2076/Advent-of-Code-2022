input = open('Day6\Input_Day6.txt').read()

def pack_marker(marker_value):
    for i in range(len(input)):
        set_char = input[i:i+marker_value]
        if len(set(set_char)) == len(set_char):
            a = input.rindex(set_char) + marker_value
            break
    return a

#Part 1 start of message marker 4
print(f"PART 1: the number of characters needed to be processed to detect the start-of-packet marker is : {pack_marker(4)}")

#Part 2 start of message marker 14
print(f"PART 2: the number of characters needed to be processed to detect the start-of-packet marker is : {pack_marker(14)}")
        
