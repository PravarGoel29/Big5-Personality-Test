


string1 = 'marr'
string2 = 'div'
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

            divDate = lines[i + 3]
            divDateSplit = str.split(divDate)
            divDateSplit[2] = ' '.join(divDateSplit[2:])
            FinaldivDate = pardivDateSplit[2]
            FinaldivDateList = []
            FinaldivDateList.append(FinaldivDate)
            # print(FinaldivDateList)
            print('parent divorce date:' + FinaldivDate)
            pardivDateArray = str.split(FinaldivDate)
            FinaldivYear = divDateArray[2]
            FinaldivYearList = []
            FinaldivYearList.append(FinaldivYear)
            # print(FinaldivYearList)
            if FinalmarrYear < FinaldivYear and FinalmarrDate != FinaldivDate:
                print('marriage year < divorce year')

            else:
                print('This situation is invalid')

        i += 1


