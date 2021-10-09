from prettytable import PrettyTable
import datetime

GedcomTable = PrettyTable(["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death"])
FamilyTable = PrettyTable(["ID", "Married", "Divorced", "Husband ID", "Wife ID", "Children"])

with open('/Users/pravar/Downloads/Family-4-19-Sep-2021-014639122 (2).ged') as f:
    lines = f.readlines()

i = 0
j = 0
k = 0
ChildID = ''
ChildID2 = ''
ChildID3 = ''
HusbandNameLine = ''
WifeNameLine = ''
HusbID = ''
IDName = []
ID = ''
Name = ''

for line in lines:
    if '0 I' in line:
        IDLine = lines[i]
        IDLineSplit = str.split(IDLine)
        ID = IDLineSplit[1]
        #print(ID)  # ID
        NameLine = lines[i + 1]
        NameLineSplit = str.split(NameLine)
        NameLineSplit[2] = ' '.join(NameLineSplit[2:])
        Name = NameLineSplit[2]


        #print(IDName)
        #print(Name)  # name
        SexLine = lines[i + 2]  # sex
        SexLineSplit = str.split(SexLine)
        Sex = SexLineSplit[2]

        #print(Sex)
        BirthDateLine = lines[i + 4]  # birthday
        BirthDateLineSplit = str.split(BirthDateLine)
        if BirthDateLineSplit[3] == 'JAN':
            BirthDateLineSplit[3] = '01'
        elif BirthDateLineSplit[3] == 'FEB':
            BirthDateLineSplit[3] = '02'
        elif BirthDateLineSplit[3] == 'MAR':
            BirthDateLineSplit[3] = '03'
        elif BirthDateLineSplit[3] == 'APR':
            BirthDateLineSplit[3] = '04'
        elif BirthDateLineSplit[3] == 'MAY':
            BirthDateLineSplit[3] = '05'
        elif BirthDateLineSplit[3] == 'JUN':
            BirthDateLineSplit[3] = '06'
        elif BirthDateLineSplit[3] == 'JUL':
            BirthDateLineSplit[3] = '07'
        elif BirthDateLineSplit[3] == 'AUG':
            BirthDateLineSplit[3] = '08'
        elif BirthDateLineSplit[3] == 'SEP':
            BirthDateLineSplit[3] = '09'
        elif BirthDateLineSplit[3] == 'OCT':
            BirthDateLineSplit[3] = '10'
        elif BirthDateLineSplit[3] == 'NOV':
            BirthDateLineSplit[3] = '11'
        elif BirthDateLineSplit[3] == 'DEC':
            BirthDateLineSplit[3] = '12'

        BirthString = BirthDateLineSplit[4] + '-' + BirthDateLineSplit[3] + '-' + BirthDateLineSplit[2]
        #print(BirthString)

        Age = 2021 - int(BirthDateLineSplit[4])
        #print(Age)  # age

        if 'DEAT' in lines[i + 5]:
            Alive = 'FALSE'
            DeathDateLine = lines[i + 6]
            DeathDateLineSplit = str.split(DeathDateLine)
            Deathday = DeathDateLineSplit[4] + '-' + DeathDateLineSplit[3] + '-' + DeathDateLineSplit[2]
            #print(Deathday)

        else:
            Alive = 'TRUE'
            Deathday = 'NA'
            #print(Deathday)

        #print(Alive)
        GedcomTable.add_row([ID, Name, Sex, BirthString, Age, Alive, Deathday])


    #print(IDName)

        if Sex == 'M':

            HusbName = Name
            #print(HusbName)

        else:
            WifeName = Name

    i += 1
    if '0 F0' in line:
        FamilyIDLine = lines[j]
        #print(FamilyIDLine)
        FamilyIDLineSplit = str.split(FamilyIDLine)
        FamilyID = FamilyIDLineSplit[1]
        #print(FamilyID)

        HusbIDLine = lines[j+1]
        #print(HusbIDLine)
        HusbIDLineSplit = str.split(HusbIDLine)
        HusbID = HusbIDLineSplit[2]


        #print(HusbandNameLine)

        WifeIDLine = lines[j+2]
        WifeIDLineSplit = str.split(WifeIDLine)
        WifeID = WifeIDLineSplit[2]
        WifeNameLine = '0 ' + WifeID


        if '1 CHIL' in lines[j+3]:
            ChildIDLine = lines[i+2]
            ChildIDLineSplit = str.split(ChildIDLine)
            ChildID = ChildIDLineSplit[2]
            #print(ChildID)
        if '1 CHIL' in lines[j+4]:
            ChildIDLine = lines[i+3]
            ChildIDLineSplit2 = str.split(ChildIDLine)
            ChildID2 = ChildIDLineSplit2[2]
            #print(ChildID2)
        if '1 CHIL' in lines[j+5]:
            ChildIDLine = lines[i+4]
            ChildIDLineSplit3 = str.split(ChildIDLine)
            ChildID3 = ChildIDLineSplit3[2]
            #print(ChildID3)
            FinalChildID = ChildID + ', ' + ChildID2 + ', ' + ChildID3
        FinalChildID = ChildID+'  '+ChildID2+'  '+ChildID3
        #print(FinalChildID)

        #print(ChildID)
        if '1 MARR' in lines[j+4]:
            MarrDateLine = lines[j + 5]
            MarrDateLineSplit = str.split(MarrDateLine)
            if MarrDateLineSplit[3] == 'JAN':
                MarrDateLineSplit[3] = '01'
            elif MarrDateLineSplit[3] == 'FEB':
                MarrDateLineSplit[3] = '02'
            elif MarrDateLineSplit[3] == 'MAR':
                MarrDateLineSplit[3] = '03'
            elif MarrDateLineSplit[3] == 'APR':
                MarrDateLineSplit[3] = '04'
            elif MarrDateLineSplit[3] == 'MAY':
                MarrDateLineSplit[3] = '05'
            elif MarrDateLineSplit[3] == 'JUN':
                MarrDateLineSplit[3] = '06'
            elif MarrDateLineSplit[3] == 'JUL':
                MarrDateLineSplit[3] = '07'
            elif MarrDateLineSplit[3] == 'AUG':
                MarrDateLineSplit[3] = '08'
            elif MarrDateLineSplit[3] == 'SEP':
                MarrDateLineSplit[3] = '09'
            elif MarrDateLineSplit[3] == 'OCT':
                MarrDateLineSplit[3] = '10'
            elif MarrDateLineSplit[3] == 'NOV':
                MarrDateLineSplit[3] = '11'
            elif MarrDateLineSplit[3] == 'DEC':
                MarrDateLineSplit[3] = '12'
            MarrDate = MarrDateLineSplit[4] + '-' + MarrDateLineSplit[3] + '-' + MarrDateLineSplit[2]
            #print(MarrDate)
        elif '1 MARR' in lines[j+5]:
            MarrDateLine = lines[j + 6]
            MarrDateLineSplit = str.split(MarrDateLine)
            if MarrDateLineSplit[3] == 'JAN':
                MarrDateLineSplit[3] = '01'
            elif MarrDateLineSplit[3] == 'FEB':
                MarrDateLineSplit[3] = '02'
            elif MarrDateLineSplit[3] == 'MAR':
                MarrDateLineSplit[3] = '03'
            elif MarrDateLineSplit[3] == 'APR':
                MarrDateLineSplit[3] = '04'
            elif MarrDateLineSplit[3] == 'MAY':
                MarrDateLineSplit[3] = '05'
            elif MarrDateLineSplit[3] == 'JUN':
                MarrDateLineSplit[3] = '06'
            elif MarrDateLineSplit[3] == 'JUL':
                MarrDateLineSplit[3] = '07'
            elif MarrDateLineSplit[3] == 'AUG':
                MarrDateLineSplit[3] = '08'
            elif MarrDateLineSplit[3] == 'SEP':
                MarrDateLineSplit[3] = '09'
            elif MarrDateLineSplit[3] == 'OCT':
                MarrDateLineSplit[3] = '10'
            elif MarrDateLineSplit[3] == 'NOV':
                MarrDateLineSplit[3] = '11'
            elif MarrDateLineSplit[3] == 'DEC':
                MarrDateLineSplit[3] = '12'
            MarrDate = MarrDateLineSplit[4] + '-' + MarrDateLineSplit[3] + '-' + MarrDateLineSplit[2]
            #print(MarrDate)


        if '1 DIV' in line:
            DivDateLine = lines[j + 1]
            DivDateLineSplit = str.split(DivDateLine)
            DivDate = DivDateLineSplit[4] + '-' + DivDateLineSplit[3] + '-' + DivDateLineSplit[2]
            #print(DivDate)
        else:
            DivDate = 'NA'



        FamilyTable.add_row([FamilyID, MarrDate, DivDate, HusbID,  WifeID,  FinalChildID])


    j += 1
    k += 1
print(GedcomTable)
print(FamilyTable)