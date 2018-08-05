class teamdata:
	teamID = ''
	wingame = 0
	totalgame = 0
	successfieldgoal = 0
	totalfieldgoal = 0
	offRebound = 0
	defRebound = 0
	block = 0
	steal = 0
	turnOver = 0

	def read(self, data):
		self.teamID = data[0]
		self.wingame = int(data[1])
		self.totalgame = int(data[2])
		self.successfieldgoal = int(data[3])
		self.totalfieldgoal = int(data[4])
		self.offRebound = int(data[5])
		self.defRebound = int(data[6])
		self.block = int(data[7])
		self.steal = int(data[8])
		self.turnOver = int(data[9])

	def update(self, winorlose, fieldgoal, fieldgoals, OR, dr, blk, stl, TO, ID = '1100'):
		if '1100' != ID :
			self.teamID = ID
		self.totalgame = self.totalgame + 1
		if winorlose == 1:
			self.wingame = self.wingame + 1
		self.totalfieldgoal = self.totalfieldgoal + fieldgoal			
		self.successfieldgoal = self.successfieldgoal + fieldgoals
		self.offRebound = self.offRebound + OR
		self.defRebound = self.defRebound + dr
		self.block = self.block + blk
		self.steal = self.steal + stl
		self.turnOver = self.turnOver + TO

	def weight(self):
		return {
			field: fieldgoalRate,
			meanOR: offRebound,
			meanDR: defRebound,
			meanBLK: meanBlock,
			meanSTL: meanSteal,
			meanTO: meanTurnOver
		}
	
