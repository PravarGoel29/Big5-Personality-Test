def MarrAge():
    with open('/Users/pravar/Downloads/Family-4-19-Sep-2021-014639122 (2).ged') as f:
        lines = f.readlines()

    FinalCodeLineList = []
    FinalNameList = []
    FinalSexList = []
    i = 0
    for line in lines:

        if '0 I' in line:
            CodeLine = lines[i]
            CodeLineSplit = str.split(CodeLine)
            FinalCodeLine = CodeLineSplit[1]
            print(FinalCodeLine)
            FinalCodeLineList.append(FinalCodeLine)

            NameLine = lines[i + 1]
            NameLineSplit = str.split(NameLine)
            NameLineSplit[2] = ' '.join(NameLineSplit[2:])
            FinalNameLine = NameLineSplit[2]
            print(FinalNameLine)

            FinalNameList.append(FinalNameLine)

            SexLine = lines[i + 2]
            SexLineSplit = str.split(SexLine)
            FinalSexLine = SexLineSplit[2]
            print(FinalSexLine)

            FinalSexList.append(FinalSexLine)

            if FinalSexLine == 'M' and '1 HUSB '+FinalCodeLine in lines:
                print('Gender is correct')
            elif FinalSexLine == 'S' and '1 WIFE '+FinalCodeLine in lines:
                print('Gender is correct')
            else:
                print('Gender is correct')

        i += 1

    return FinalCodeLineList, FinalNameList, FinalSexList





    f.close()
MarrAge()