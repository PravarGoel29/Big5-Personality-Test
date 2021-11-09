from datetime import date

def DivDeathDate():
	with open('/Users/pravar/Downloads/Family-4-19-Sep-2021-014639122 (2).ged') as f:
		lines = f.readlines()

	FinalDateList = []
	FinalYearList = []
	i = 0
	for line in lines:

		if 'DATE' in line:
			DateSplit = str.split(line)
			DateSplit[2] = ' '.join(DateSplit[2:])
			FinalDate = DateSplit[2]
			#print(FinalDate)
			YearSplit = str.split(FinalDate)
			FinalYear = YearSplit[2]
			#print(FinalYear)
			FinalDateList.append(FinalDate)
			FinalYearList.append(FinalYear)
			today = date.today()

			if int(FinalYear) <= 2021 and FinalDate != today:
				print('Date is less than the current date')

			else:
				event = lines[i-1]
				print(lines[i - 3])
				print(event)
				print(line)
				print('Error: No date can be greater than the current date')
		i += 1
	return FinalDateList, FinalYearList, today
