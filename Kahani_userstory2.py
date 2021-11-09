string1 = 'marr'
string2 = 'death'
with open('/Users/KAHANI/Downloads/My-Family-20-Sep-2021-214410223.ged') as f:
    lines = f.readlines()

i = 0


def marrbefdiv():
    for line in lines:

        if string1 in line and string2 in lines[i + 2]:

            marrDate = lines[i + 1]
            marrDateSplit = str.split(marrDate)
            marrDateSplit[2] = ' '.join(marrDateSplit[2:])
            FinalmarrDate = marrDateSplit[2]
            FinalmarrDateList = []
            FinalmarrDateList.append(FinalmarrDate)
            print(lines[i - 2])
            # print(FinalmarrDateList)
            print('marriage date:' + FinalmarrDate)
            marrDateArray = str.split(FinalmarrDate)
            FinalmarrYear = marrDateArray[2]
            FinalmarrYearList = []
            FinalmarrYearList.append(FinalmarrYear)
            # print(FinalmarrYearList)

            deathDate = lines[i + 3]
            deathDateSplit = str.split(deathDate)
            deathDateSplit[2] = ' '.join(deathDateSplit[2:])
            FinaldeathDate = pardeathDateSplit[2]
            FinaldeathDateList = []
            FinaldeathDateList.append(FinaldeathDate)
            # print(FinaldeathDateList)
            print('parent death date:' + FinaldeathDate)
            pardeathDateArray = str.split(FinaldeathDate)
            FinaldeathYear = deathDateArray[2]
            FinaldeathYearList = []
            FinaldeathYearList.append(FinaldeathYear)
            # print(FinaldeathYearList)
            if FinalmarrYear < FinaldeathYear and FinalmarrDate != FinaldeathDate:
                print('marriage year < death year')

            else:
                print('This situation is invalid')

        i += 1
