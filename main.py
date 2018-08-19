import csv, time, os
from teamClass import teamdata

stime = time.time()

data = []
try: 
	with open('Data_2003.csv', 'r', encoding='utf-8') as f:
		rd = csv.reader(f)
		for e in rd:
			team = teamdata()
			team.read(e)
			data.append(team)
	del rd, e, team

except FileNotFoundError:
	fList = os.listdir()
	fList = [s for s in fList if "Data_" in s and ".csv" in s]
	seasons = [];
	for s in fList : seasons.append(s.strip("Data_.csv"))
	with open('RegularSeasonDetailedResults.csv', 'r', encoding='utf-8') as rf:
		rd = csv.reader(rf)
		seasonData = []; tID = []; seasonID = "2003"
		caseW = [9, 8, 14, 15, 19, 20, 17]; caseL = [num+13 for num in caseW];
		for e in rd:
			if 'Season' != e[0] not in seasons :
				if e[0] != seasonID :
					with open('Data_'+seasonID+'.csv', 'w', encoding='utf-8', newline='') as wf :
						wd = csv.writer(wf)
						for e2 in seasonData :
							wd.writerow([e2.teamID, e2.wingame, e2.totalgame, e2.successfieldgoal, e2.totalfieldgoal, e2.offRebound, e2.defRebound, e2.block, e2.steal, e2.turnOver])
					if seasonID == "2003" :
						data = seasonData.copy()
					seasonData = []; tID = [];
				s = [int(e[x]) for x in caseW] + [e[2]]
				if e[2] in tID :
					seasonData[tID.index(e[2])].update(1, *s)
				else :
					team = teamdata()
					team.update(1, *s)
					seasonData.append(team)
					tID.append(e[2])
				s = [int(e[x]) for x in caseL] + [e[4]]
				if e[4] in tID :
					seasonData[tID.index(e[4])].update(0, *s)
				else :
					team = teamdata()
					team.update(0, *s)
					seasonData.append(team)
					tID.append(e[4])
				seasonID = e[0]
		else :
			with open('Data_'+seasonID+'.csv', 'w', encoding='utf-8', newline='') as wf :
				wd = csv.writer(wf)
				for e2 in seasonData :
					wd.writerow([e2.teamID, e2.wingame, e2.totalgame, e2.successfieldgoal, e2.totalfieldgoal, e2.offRebound, e2.defRebound, e2.block, e2.steal, e2.turnOver])
	del fList, seasons, s, rd, seasonData, tID, seasonID, caseW, caseL, e, wd, e2, team

print('Total Time: ', time.time() - stime); del stime