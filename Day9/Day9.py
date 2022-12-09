from math import dist

directions = {
    'U' : (0, 1),
    'D' : (0, -1),
    'L' : (-1,0),
    'R' : (1, 0)
}

def distance(p1, p2):
    return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

def read_input(file = 'Day9\Input_Day9.txt'):
    with open(file) as f:
        return [(directions[line.split()[0]], int(line.split()[1])) for line in f.readlines()]
    
def exec_moves(move, body_pos, tail_visit_overview):
    dirs, step = move
    for _ in range(step):
        body_pos[0] = (body_pos[0][0] + dirs[0],
                       body_pos[0][1] + dirs[1])

        for i in range(1, len(body_pos)):
            if distance(body_pos[i], body_pos[i-1]) > 1:
                new_x, new_y = body_pos[i]
                if body_pos[i][0] != body_pos[i-1][0]:
                    new_x += (body_pos[i-1][0] - body_pos[i][0]) / \
                        abs((body_pos[i - 1][0] - body_pos[i][0]))
                if body_pos[i][1] != body_pos[i-1][1]:
                    new_y += (body_pos[i-1][1] - body_pos[i][1]) / \
                        abs((body_pos[i - 1][1] - body_pos[i][1]))
                body_pos[i] = (new_x, new_y)
        tail_visit_overview[body_pos[-1]] = True
    return body_pos

def solve(moves, body_length):
    body_pos = [(0, 0) for _ in range(body_length)]
    tail_visit_overview = {body_pos[-1]: True}
    for move in moves:
        body_pos = exec_moves(move, body_pos, tail_visit_overview)
    return len(tail_visit_overview)

# if __name__ == "__main__":
#     print("For debugging:")
#     moves = read_input()
#     print(f"moves[0]: {moves[0]}")
#     print(f"moves[1]: {moves[1]}")
#     print("...")
#     print(f"moves[-1]: {moves[-1]}")
#     print()

moves = read_input()
    print(f"moves[0]: {moves[0]}")
    print(f"moves[1]: {moves[1]}")
    print("...")
    print(f"moves[-1]: {moves[-1]}")
    print()

print(f"Part 1: tail visited total {solve(moves, 2)} unique places")
print(f"Part 2: tail visited total {solve(moves, 10)} unique places")