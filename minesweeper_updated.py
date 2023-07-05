#first define a mine sweeper function
def mine_sweeper(grid):

#the function should check every spot in the grid
#set up the loop to go through each spot in the grid
    for rows in range(len(grid)):
        for cols in range(len(grid[rows])):

#if the spot is not a mine, the adjacent mines should be counted
            if grid[rows][cols] == "-" :
                count = 0 #set up the initial adjucent mine

#check horizontally, vertically, and diagonally adjacent spots
                for i in range(max(0,rows-1), min(len(grid),rows+2)):
                    for j in range(max(0,cols-1), min(len(grid[rows]),cols+2)):
                        if grid[i][j] == "#":
                            count += 1

#set the spot in the result grid to the count
                grid[rows][cols] = str(count)

#return the result grid
    return grid

#example usage:
print("Start new mine sweeping!")
#input a mine grid to start the sweeping function
print("Your mine grid:")
grid = [["-", "-", "-", "#", "#"],["-", "#", "-", "-", "-"],["-", "-", "#", "-", "-"],["-", "#", "#", "-", "-"],["-", "-", "-", "-", "-"]]
for n in range(0,len(grid)):
    print(grid[n])

result = mine_sweeper(grid)

print("Your mine sweeping result:")
for n in range(0,len(grid)):
    print(result[n])

