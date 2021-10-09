string1 = 'BIRT'
string2 = 'DEAT'

with open('/Users/pravar/Downloads/Family-4-19-Sep-2021-014639122 (2).ged') as f:
	lines = f.readlines()

i = 0
FinalBirthDateList = []
FinalBirthYearList = []
FinalDeathDateList = []
FinalDeathYearList = []
for line in lines:

    if string1 in line and string2 in lines[i+2]:

        BirthDate = lines[i+1]
        BirthDateSplit = str.split(BirthDate)
        BirthDateSplit[2] = ' '.join(BirthDateSplit[2:])
        FinalBirthDate = BirthDateSplit[2]

        FinalBirthDateList.append(FinalBirthDate)
        print(lines[i-2])
        #print(FinalBirthDateList)
        print('Birth date:'+FinalBirthDate)
        BirthDateArray = str.split(FinalBirthDate)
        FinalBirthYear = BirthDateArray[2]

        FinalBirthYearList.append(FinalBirthYear)
        #print(FinalBirthYearList)

        DeathDate = lines[i+3]
        DeathDateSplit = str.split(DeathDate)
        DeathDateSplit[2] = ' '.join(DeathDateSplit[2:])
        FinalDeathDate = DeathDateSplit[2]

        FinalDeathDateList.append(FinalDeathDate)
        #print(FinalDeathDateList)
        print('Death date:'+FinalDeathDate)
        DeathDateArray = str.split(FinalDeathDate)
        FinalDeathYear = DeathDateArray[2]

        FinalDeathYearList.append(FinalDeathYear)
        #print(FinalDeathYearList)
        if FinalBirthYear < FinalDeathYear and FinalBirthDate != FinalDeathDate:
            print('Birth year < Death year')

        else:
            print('Error: Birth year cannot be greater than death year')

    i += 1




