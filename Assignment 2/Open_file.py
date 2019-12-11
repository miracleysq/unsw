class Maze():
	# 打开文件 生成矩阵
	def __init__(self,file):
		self.dots = []
		with open(file) as files:
			for line in files:
				if line != '\n' :
					row = []
					for e in ''.join(line.strip().split()):
						row.append(int(e))
					if row:
						self.dots.append(row)
		self.dots_row = len(self.dots)
		self.dots_col = len(self.dots[0])

	def __str__(self):
		return f'Maze({self.dots})'
	def __repr__(self):
		return f'Maze({self.dots})'
	#分析矩阵
	def analyse_gates(self):
		self.gates=0
		self.gates_value=[]
		for j in range(self.dots_col-1):		# 分析 上边的门
			if self.dots[0][j] == 0 or self.dots[0][j] == 2:
				self.gates += 1
				self.gates_value.append((0,j))
		for j in range(self.dots_col-1):		# 分析 下边的门
			if self.dots[-1][j] != 1:
				self.gates += 1	
				self.gates_value.append((self.dots_row-2,j))
		for i in range(self.dots_row-1):		# 分析 左边
			if self.dots[i][0] == 0 or self.dots[i][0] == 1:
				self.gates += 1
				self.gates_value.append((i,0))
		for i in range(self.dots_row-1):		# 分析 右边
			if self.dots[i][-1] != 2:
					self.gates += 1
					self.gates_value.append((i,self.dots_col-2))
		return self.gates
	def display_gates_value(self):		#返回所有的门的坐标
		return self.gates_value

	def check_connect_dots(self,dot):			#判断 线段是否相连
		(i,j) = dot
		dots_row = self.dots_row
		dots_col = self.dots_col
		grid = self.dots
		if 0<= i <= dots_row and 0 <= j <= dots_col:
			if dot not in self.checked_dot:
				self.checked_dot.append(dot)
				if 0<= i <= dots_row and 0 <= j <= dots_col:
					if grid[i][j]==1:	#判断左,右,上 + 右上 四边
						if 0 <= j-1 <= dots_col:	#左边
							if grid[i][j-1] == 1 or grid[i][j-1] == 3:
								self.check_connect_dots((i,j-1))
						if 0 <= j+1 <= dots_col:	#右边
							if grid[i][j+1] == 1 or grid[i][j+1] ==2 or grid[i][j+1] == 3:
								self.check_connect_dots((i,j+1))
						if 0 <= i-1 <= dots_row:	#上边
							if grid[i-1][j] == 2 or grid[i-1][j] ==3:
								self.check_connect_dots((i-1,j))
						if 0<= i-1<= dots_row and 0<= j+1<= dots_col:	#右上
							if grid[i-1][j+1] == 2 or grid[i-1][j+1] ==3:
								self.check_connect_dots((i-1,j+1))
					if grid[i][j]==2:	#判断左，上，下 + 左下 四边
						if 0<= j-1 <= dots_col:		#左边
							if grid[i][j-1] == 1 or grid[i][j-1]==3:
								self.check_connect_dots((i,j-1))
						if 0 <= i-1 <= dots_row : 	#上边
							if grid[i-1][j] == 2 or grid[i-1][j] == 3:
								self.check_connect_dots((i-1,j))
						if 0 <= i+1 <= dots_row:	#下边
							if grid[i+1][j] == 2 or grid[i+1][j] == 3 or grid[i+1][j] == 1:
								self.check_connect_dots((i+1,j))
						if 0<= i+1<= dots_row and 0<= j-1<= dots_col:	#左下
							if grid[i+1][j-1] ==1 or grid[i+1][j-1] == 3:
								self.check_connect_dots((i+1,j-1))
					if grid[i][j] == 3:		#判断左，右，上，下 + 右上，左下 六边
						if 0<= j-1 <= dots_col:		#左边
							if grid[i][j-1] ==1 or grid[i][j-1] ==3:
								self.check_connect_dots((i,j-1))
						if 0 <= j+1 <= dots_col:	#右边
							if grid[i][j+1] == 1 or grid[i][j+1] ==2 or grid[i][j+1] ==3:
								self.check_connect_dots((i,j+1))
						if 0 <= i-1 <= dots_row:	#上边
							if grid[i-1][j] == 2 or grid[i-1][j] == 3:
								self.check_connect_dots((i-1,j))
						if 0 <= i+1 <= dots_row:	#下边
							if grid[i+1][j] == 1 or grid[i+1][j] ==2 or grid[i+1][j] ==3:
								self.check_connect_dots((i+1,j))
						if 0<= i+1<= dots_row and 0<= j-1<= dots_col:	#左下
							if grid[i+1][j-1] ==1 or grid[i+1][j-1] == 3:
								self.check_connect_dots((i+1,j-1))
						if 0<= i-1<= dots_row and 0<= j+1 <= dots_col:	#右上
							if grid[i-1][j+1]== 2 or grid[i-1][j+1]== 3:
								self.check_connect_dots((i-1,j+1))		
	def analyse_connect_walls(self):
		self.walls = 0
		self.checked_dot = []
		for i in range(self.dots_row):
			for j in range(self.dots_col):
				if self.dots[i][j]!= 0: 
					if (i,j) not in self.checked_dot:
						self.walls +=1
						self.check_connect_dots((i,j))
		return self.walls

	def check_connect_cells(self,cell):			#判断 方块是否相通
		(i,j) = cell
		dots_row = self.dots_row
		dots_col = self.dots_col
		grid = self.dots
		if 0<= i <= dots_row-1 and 0 <= j <= dots_col-1:
			if cell not in self.checked_cell:
				self.checked_cell.append(cell)
				if 0<= i <= dots_row-1 and 0 <= j <= dots_col-1:
					if grid[i][j]==0:
						if 0 <= j-1 <= dots_col-1:		#左
							self.check_connect_cells((i,j-1))
						if 0 <= j+1 <= dots_col-2:		#右
							if grid[i][j+1]==1 or grid[i][j+1]== 0:
								self.check_connect_cells((i,j+1))
						if 0<= i-1 <= dots_row-1:		#上
							self.check_connect_cells((i-1,j))
						if 0<= i+1 <= dots_row-2:		#下
							if grid[i+1][j]== 0 or grid[i+1][j]== 2:
								self.check_connect_cells((i+1,j))
					if grid[i][j]==1:	#判断左，右，下 三边
						if 0 <= j-1 <= dots_col-1:		#左
							self.check_connect_cells((i,j-1))
						if 0 <= j+1 <= dots_col-2:		#右
							if grid[i][j+1]==1 or grid[i][j+1]== 0:
								self.check_connect_cells((i,j+1))
						if 0<= i+1 <= dots_row-2:		#下
							if grid[i+1][j]== 0 or grid[i+1][j]== 2:
								self.check_connect_cells((i+1,j))
					if grid[i][j] == 2:		#判断上，下，右 三边
						if 0<= i-1 <= dots_row-1:		#上
							self.check_connect_cells((i-1,j)) 
						if 0<= i+1 <= dots_row-2:		#下
							if grid[i+1][j]== 0 or grid[i+1][j]== 2:
								self.check_connect_cells((i+1,j))
						if 0 <= j+1 <= dots_col-2:		#右
							if grid[i][j+1]==1 or grid[i][j+1]== 0:
								self.check_connect_cells((i,j+1))
					if grid[i][j] == 3:		#判断下，右 两边
						if 0<= i+1 <= dots_row-2:		#下
							if grid[i+1][j]== 0 or grid[i+1][j]== 2:
								self.check_connect_cells((i+1,j))
						if 0 <= j+1 <= dots_col-2:		#右
							if grid[i][j+1]==1 or grid[i][j+1]== 0:
								self.check_connect_cells((i,j+1))
	def analyse_connect_areas(self):
		self.areas=0
		self.checked_cell=[]
		for i in range(self.dots_row-1):
			for j in range(self.dots_col-1):
				if (i,j) in self.gates_value:
					if (i,j) not in self.checked_cell:
						self.areas +=1
						self.check_connect_cells((i,j))
		return self.areas
	def analyse_inner_points(self):
		all_cells= (self.dots_col-1) * (self.dots_row-1)
		self.inner_points = all_cells - len(self.checked_cell)
		return self.inner_points

	def all_possible_paths(self,from_cell,to_cell,pre_path):
		global paths
		if from_cell == to_cell:
			paths.append(pre_path + [to_cell])
			return
		(i,j)= from_cell
		dots_row = self.dots_row
		dots_col = self.dots_col
		grid = self.dots
		if 0<= i <= dots_row-1 and 0 <= j <= dots_col-1:
			if from_cell not in pre_path:
				if grid[i][j]==0:
						if 0 <= j-1 <= dots_col-1:		#左
							self.all_possible_paths((i,j-1),to_cell,pre_path+[from_cell])
						if 0 <= j+1 <= dots_col-2:		#右
							if grid[i][j+1]==1 or grid[i][j+1]== 0:
								self.all_possible_paths((i,j+1),to_cell,pre_path+[from_cell])
						if 0<= i-1 <= dots_row-1:		#上
							self.all_possible_paths((i-1,j),to_cell,pre_path+[from_cell])
						if 0<= i+1 <= dots_row-2:		#下
							if grid[i+1][j]== 0 or grid[i+1][j]== 2:
								self.all_possible_paths((i+1,j),to_cell,pre_path+[from_cell])
				if grid[i][j]==1:	#判断左，右，下 三边
						if 0 <= j-1 <= dots_col-1:		#左
							self.all_possible_paths((i,j-1),to_cell,pre_path+[from_cell])
						if 0 <= j+1 <= dots_col-2:		#右
							if grid[i][j+1]==1 or grid[i][j+1]== 0:
								self.all_possible_paths((i,j+1),to_cell,pre_path+[from_cell])
						if 0<= i+1 <= dots_row-2:		#下
							if grid[i+1][j]== 0 or grid[i+1][j]== 2:
								self.all_possible_paths((i+1,j),to_cell,pre_path+[from_cell])
				if grid[i][j] == 2:		#判断上，下，右 三边
						if 0<= i-1 <= dots_row-1:		#上
							self.all_possible_paths((i-1,j),to_cell,pre_path+[from_cell])
						if 0<= i+1 <= dots_row-2:		#下
							if grid[i+1][j]== 0 or grid[i+1][j]== 2:
								self.all_possible_paths((i+1,j),to_cell,pre_path+[from_cell])
						if 0 <= j+1 <= dots_col-2:		#右
							if grid[i][j+1]==1 or grid[i][j+1]== 0:
								self.all_possible_paths((i,j+1),to_cell,pre_path+[from_cell])
				if grid[i][j] == 3:		#判断下，右 两边
						if 0<= i+1 <= dots_row-2:		#下
							if grid[i+1][j]== 0 or grid[i+1][j]== 2:
								self.all_possible_paths((i+1,j),to_cell,pre_path+[from_cell])
						if 0 <= j+1 <= dots_col-2:		#右
							if grid[i][j+1]==1 or grid[i][j+1]== 0:
								self.all_possible_paths((i,j+1),to_cell,pre_path+[from_cell])

	def analyse_paths(self):
		global paths
		gates = self.gates_value
		for i in range(len(gates)):
			for j in range(i+1,len(gates)):
				self.all_possible_paths(gates[i],gates[j],[])
		return paths

	def find_all_cul_de_sacs(self):
		record=[]
		self.cul_de_sacs_points=[]
		dots_row = self.dots_row
		dots_col = self.dots_col
		for i in paths:
			for j in i:
				record.append(j)
		set_record = set(record)
		for i in self.checked_cell:
			if i not in set_record:
				self.cul_de_sacs_points.append(i)
#		print(self.cul_de_sacs_points)
		return self.cul_de_sacs_points
	def check_connect_cul_de_sacs(self,cell):
		(i,j) = cell
		dots_row = self.dots_row
		dots_col = self.dots_col
		grid = self.dots
		if 0<= i <= dots_row-1 and 0 <= j <= dots_col-1:
			if cell not in self.checked_cell:
					self.checked_cell.append(cell)
					if grid[i][j]==0:
						if 0 <= j-1 <= dots_col-1 and (i,j-1) in self.cul_de_sacs_points:		#左
							self.check_connect_cul_de_sacs((i,j-1))
						if 0 <= j+1 <= dots_col-2 and (i,j+1) in self.cul_de_sacs_points:		#右
							if grid[i][j+1]==1 or grid[i][j+1]== 0:
								self.check_connect_cul_de_sacs((i,j+1))
						if 0<= i-1 <= dots_row-1 and (i-1,j) in self.cul_de_sacs_points:		#上
							self.check_connect_cul_de_sacs((i-1,j))
						if 0<= i+1 <= dots_row-2 and (i+1,j) in self.cul_de_sacs_points:		#下
							if grid[i+1][j]== 0 or grid[i+1][j]== 2:
								self.check_connect_cul_de_sacs((i+1,j))
					if grid[i][j]==1:	#判断左，右，下 三边
						if 0 <= j-1 <= dots_col-1 and (i,j-1) in self.cul_de_sacs_points:		#左
							self.check_connect_cul_de_sacs((i,j-1))
						if 0 <= j+1 <= dots_col-2 and (i,j+1) in self.cul_de_sacs_points:		#右
							if grid[i][j+1]==1 or grid[i][j+1]== 0:
								self.check_connect_cul_de_sacs((i,j+1))
						if 0<= i+1 <= dots_row-2 and (i+1,j) in self.cul_de_sacs_points:		#下
							if grid[i+1][j]== 0 or grid[i+1][j]== 2:
								self.check_connect_cul_de_sacs((i+1,j))
					if grid[i][j] == 2:		#判断上，下，右 三边
						if 0<= i-1 <= dots_row-1 and (i-1,j) in self.cul_de_sacs_points:		#上
							self.check_connect_cul_de_sacs((i-1,j)) 
						if 0<= i+1 <= dots_row-2 and (i+1,j) in self.cul_de_sacs_points:		#下
							if grid[i+1][j]== 0 or grid[i+1][j]== 2:
								self.check_connect_cul_de_sacs((i+1,j))
						if 0 <= j+1 <= dots_col-2 and (i,j+1) in self.cul_de_sacs_points:		#右
							if grid[i][j+1]==1 or grid[i][j+1]== 0:
								self.check_connect_cul_de_sacs((i,j+1))
					if grid[i][j] == 3:		#判断下，右 两边
						if 0<= i+1 <= dots_row-2 and (i+1,j) in self.cul_de_sacs_points:		#下
							if grid[i+1][j]== 0 or grid[i+1][j]== 2:
								self.check_connect_cul_de_sacs((i+1,j))
						if 0 <= j+1 <= dots_col-2 and (i,j+1) in self.cul_de_sacs_points:		#右
							if grid[i][j+1]==1 or grid[i][j+1]== 0:
								self.check_connect_cul_de_sacs((i,j+1))
	def analyse_cul_de_sacs(self):
		self.cul_de_sacs_areas=0
		self.checked_cell = []
		for i in self.cul_de_sacs_points:
			if i not in self.checked_cell:
				self.cul_de_sacs_areas+= 1
				self.check_connect_cul_de_sacs(i)
		return self.cul_de_sacs_areas

	def analyse_unique_path(self):
		gate = []
		self.unique_path=[]
		global paths
		for i in self.gates_value:
			if i not in self.cul_de_sacs_points:
				gate.append(i)
		for i in gate:
			paths=[]
			gate_1= gate[:]
			gate_1.remove(i)
			for j in gate_1:
				self.all_possible_paths(i,j,[])
			if len(paths)== 1:
				self.unique_path.append(paths[0])
		return len(self.unique_path)//2

paths=[]
maze1= Maze('maze_2.txt')
print(maze1.analyse_gates())
print(maze1.analyse_connect_walls())
maze1.display_gates_value()
maze1.analyse_connect_areas()
print(maze1.analyse_inner_points())
print(maze1.analyse_connect_areas())
maze1.analyse_paths()
maze1.find_all_cul_de_sacs()
print(maze1.analyse_cul_de_sacs())
print(maze1.analyse_unique_path())