
def DivDeathDate(x, Datestr1, Datestr2):
	with open('/Users/pravar/Downloads/Family-4-19-Sep-2021-014639122 (2).ged') as f:
		lines = f.readlines()

	FinalDivDateList = []
	FinalDivYearList = []
	FinalDeathDateList = []
	FinalDeathYearList = []
	FinalIndiCodeList = []
	i = 0
	j = 0
	for line in lines:

		if x in line:

			print(lines[i - 4])
			IndiCode = str.split(lines[i-5])
			FinalIndiCode = IndiCode[1]
			FinalIndiCodeList.append(FinalIndiCode)
			DeathDate = lines[i + 1]
			DeathDateSplit = str.split(DeathDate)
			DeathDateSplit[2] = ' '.join(DeathDateSplit[2:])
			FinalDeathDate = DeathDateSplit[2]

			FinalDeathDateList.append(FinalDeathDate)

			print(Datestr2 + ': ' + FinalDeathDate)
			# print(Datestr1 + ': ' + FinalDivDate)
			DeathDateArray = str.split(FinalDeathDate)
			FinalDeathYear = DeathDateArray[2]

			FinalDeathYearList.append(FinalDeathYear)

			for line in lines:
				if '1 HUSB '+FinalIndiCode in line:
					if 'DIV' in lines[j+6]:
						#print(lines[j+7])
						DivDateSplit = str.split(lines[j+7])
						DivDateSplit[2] = ' '.join(DivDateSplit[2:])
						FinalDivDate = DivDateSplit[2]
						#print(FinalDivDate)
						FinalDivDateList.append(FinalDivDate)
						FinalDivYear = DivDateSplit[4]
						FinalDivYearList.append(FinalDivYear)
						if FinalDivYear < FinalDeathYear and FinalDeathDate != FinalDivDate:
							print(Datestr1 + ' < ' + Datestr2)

						else:
							print('Error:' + Datestr1 + ' cannot be greater than ' + Datestr2)

					elif 'DIV' in lines[j + 5]:
						#print(lines[j+6])
						DivDateSplit = str.split(lines[j + 6])
						DivDateSplit[2] = ' '.join(DivDateSplit[2:])
						FinalDivDate = DivDateSplit[2]
						# print(FinalDivDate)
						FinalDivDateList.append(FinalDivDate)
						FinalDivYear = DivDateSplit[4]
						FinalDivYearList.append(FinalDivYear)
						if FinalDivYear < FinalDeathYear and FinalDeathDate != FinalDivDate:
							print(Datestr1 + ' < ' + Datestr2)

						else:
							print('Error:' + Datestr1 + ' cannot be greater than ' + Datestr2)
					break
				elif '1 WIFE '+FinalIndiCode in line:
					if 'DIV' in lines[j+5]:
						#print(lines[j+6])
						DivDateSplit = str.split(lines[j + 6])
						DivDateSplit[2] = ' '.join(DivDateSplit[2:])
						FinalDivDate = DivDateSplit[2]
						#print(FinalDivDate)
						FinalDivDateList.append(FinalDivDate)
						FinalDivYear = DivDateSplit[4]
						FinalDivYearList.append(FinalDivYear)
						if FinalDivYear < FinalDeathYear and FinalDeathDate != FinalDivDate:
							print(Datestr1 + ' < ' + Datestr2)

						else:
							print('Error:' + Datestr1 + ' cannot be greater than ' + Datestr2)
					elif 'DIV' in lines[j+4]:
						#print(lines[j+5])
						DivDateSplit = str.split(lines[j + 5])
						DivDateSplit[2] = ' '.join(DivDateSplit[2:])
						FinalDivDate = DivDateSplit[2]
						#print(FinalDivDate)
						FinalDivDateList.append(FinalDivDate)
						FinalDivYear = DivDateSplit[4]
						FinalDivYearList.append(FinalDivYear)
						if FinalDivYear < FinalDeathYear and FinalDeathDate != FinalDivDate:
							print(Datestr1 + ' < ' + Datestr2)

						else:
							print('Error:' + Datestr1 + ' cannot be greater than ' + Datestr2)
					break

				j += 1




		i += 1

	return FinalDeathDateList, FinalDeathYearList, FinalDeathDateList, FinalDeathYearList, FinalIndiCode

	f.close()
DivDeathDate('DEAT','Divorce Date','Death Date')
