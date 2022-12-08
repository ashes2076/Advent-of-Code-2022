import numpy as np
import itertools

grid = np.array([list(d.strip()) for d in open('Day8\Input_Day8.txt', 'r').readlines()], dtype=int)
rows, cols = grid.shape
Visibility = 0 #Part 1
visibility_score = [] #Part 2

#Part1
for r, c in itertools.product(range(rows), range(rows)):
    tree = grid[r,c]
    if r == 0 or c == 0 or r == rows-1 or c == cols-1:
        Visibility += 1
        continue
    if np.all(grid[r, :c] < tree):
        Visibility +=1
        continue
    if np.all(grid[r, c+1:] < tree):
        Visibility += 1
        continue
    if np.all(grid[:r, c] < tree):
        Visibility += 1
        continue
    if np.all(grid[r+1:,c] < tree):
        Visibility += 1
        continue

print(f" PART 1:Number of trees visible from outside the grid is {Visibility}")


#Part 2
for r, c in itertools.product(range(rows), range(rows)):
    tree = grid[r,c]
    if r == 0 or c == 0 or r == rows-1 or c == cols-1:
        visibility_score.append(0)
        continue
    
    lv = 0
    for col in range(c-1, -1, -1):
        lv += 1
        if grid[r,col] >= tree:
            break
    rv = 0
    for col in range(c+1, cols):
        rv += 1
        if grid[r,col] >= tree:
            break
    tv = 0
    for row in range(r-1, -1, -1):
        tv += 1
        if grid[row,c] >= tree:
            break
    bv = 0
    for row in range(r+1, rows):
        bv += 1
        if grid[row,c] >= tree:
            break

    view_score = lv * rv * tv * bv
    visibility_score.append(view_score)

print(f" PART 2:Highest scenic score possible for the grid is {max(visibility_score)}")