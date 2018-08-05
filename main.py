import csv
import time
from teamClass import teamdata

data = []
stime = time.time()
try: 
	with open('OurResults.csv', 'r', encoding='utf-8') as f:
		rd = csv.reader(f)
		for e in rd:
			team = teamdata()
			team.read(e)
			data.append(team)

except FileNotFoundError:
	with open('RegularSeasonDetailedResults.csv', 'r', encoding='utf-8') as f:
		rd = csv.reader(f)
		for e in rd:
			if e[0] == 'Season':
				pass
			else :
				wchecker = False
				dchecker = False
				for d in data:
					if d.teamID == e[2]:
						wchecker = True
						d.update(winorlose = 1, fieldgoal = int(e[9]), fieldgoals = int(e[8]), OR = int(e[14]), dr = int(e[15]), blk = int(e[19]), stl = int(e[20]), TO = int(e[17]))
					elif d.teamID == e[4]:
						dchecker = True
						d.update(winorlose = 0, fieldgoal = int(e[22]), fieldgoals = int(e[21]), OR = int(e[27]), dr = int(e[28]), blk = int(e[32]), stl = int(e[33]), TO = int(e[30]))
				if wchecker == False:
					winteam = teamdata()
					winteam.update(1, int(e[9]), int(e[8]), int(e[14]), int(e[15]), int(e[19]), int(e[20]), int(e[17]), ID = e[2])
					data.append(winteam)

				if dchecker == False:
					loseteam = teamdata()
					loseteam.update(0, int(e[22]), int(e[21]), int(e[27]), int(e[28]), int(e[32]), int(e[33]), int(e[30]), ID = e[4])
					data.append(loseteam)
del rd
etime = time.time()
print('Readdata: ', data[0].teamID)
print('Total Time: ', etime - stime)

with open('OurResults.csv', 'w', encoding='utf-8', newline='') as f:
	wd = csv.writer(f)
	for e in data:
		wd.writerow([e.teamID, e.wingame, e.totalgame, e.successfieldgoal, e.totalfieldgoal, e.offRebound, e.defRebound, e.block, e.steal, e.turnOver])
