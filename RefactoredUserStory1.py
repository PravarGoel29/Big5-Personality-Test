from gedcom.parser import Parser
import datetime


def BirthDeathDate(x, y, Datestr1, Datestr2):
	with open('/Users/pravar/Downloads/Family-4-19-Sep-2021-014639122 (2).ged') as f:
		lines = f.readlines()

	FinalLDateList = []
	FinalLYearList = []
	FinalGDateList = []
	FinalGYearList = []

	i = 0
	for line in lines:

		if x in line and y in lines[i + 2]:

			LDate = lines[i + 1]
			LDateSplit = str.split(LDate)
			LDateSplit[2] = ' '.join(LDateSplit[2:])
			FinalLDate = LDateSplit[2]

			FinalLDateList.append(FinalLDate)
			if '0 F' in lines[i - 4]:
				FamilyCodeLine = str.split(lines[i - 4])
				FamilyCode = FamilyCodeLine[1]
				print(FamilyCode)
			elif '0 F' in lines[i - 5]:
				FamilyCodeLine = str.split(lines[i - 5])
				FamilyCode = FamilyCodeLine[1]
				print(FamilyCode)
			else:
				print(lines[i - 2])
			# print(FinalBirthDateList)
			print(Datestr1+': ' + FinalLDate)
			LDateArray = str.split(FinalLDate)
			FinalLYear = LDateArray[2]

			FinalLYearList.append(FinalLYear)
			# print(FinalBirthYearList)

			GDate = lines[i + 3]
			GDateSplit = str.split(GDate)
			GDateSplit[2] = ' '.join(GDateSplit[2:])
			FinalGDate = GDateSplit[2]

			FinalGDateList.append(FinalGDate)
			# print(FinalDeathDateList)
			print(Datestr2+': ' + FinalGDate)
			GDateArray = str.split(FinalGDate)
			FinalGYear = GDateArray[2]

			FinalGYearList.append(FinalGYear)
			# print(FinalDeathYearList)
			if FinalLYear < FinalGYear and FinalLDate != FinalGDate:
				print(Datestr1 +' < '+ Datestr2)

			else:
				print('Error:'+Datestr1+'cannot be greater than'+Datestr2)

		i += 1

	f.close()
	return FinalLDateList,FinalLYearList,FinalGDateList,FinalGYearList
