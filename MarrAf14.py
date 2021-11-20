def MarrAge():
    with open('/Users/pravar/Downloads/Family-4-19-Sep-2021-014639122 (2).ged') as f:
        lines = f.readlines()

    FinalMarrDateList = []
    FinalMarrYearList = []
    i = 0
    for line in lines:

        if 'MARR' in line:
            MarrDate = lines[i + 1]
            MarrDateSplit = str.split(MarrDate)
            MarrDateSplit[2] = ' '.join(MarrDateSplit[2:])
            FinalMarrDate = MarrDateSplit[2]

            FinalMarrDateList.append(FinalMarrDate)

            print('Marriage Date: ' + FinalMarrDate)
            # print(Datestr1 + ': ' + FinalDivDate)
            MarrDateArray = str.split(FinalMarrDate)
            FinalMarrYear = MarrDateArray[2]

            FinalMarrYearList.append(FinalMarrYear)

            if int(FinalMarrYear) < 14:
                print('Error: Marriage under 14 years')
            else:
                print('Marriage age > 14')

        i += 1

    return FinalMarrYearList, FinalMarrDateList

    f.close()