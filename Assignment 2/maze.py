maze = []
with open('maze_1.txt') as file:
	for line in file:
		if line != '\n' :
			row = []
			for e in line.strip().split():
				row.append(e)
			if row:
				maze.append(row)
print(maze)
