#!/usr/bin/env python
# coding: utf-8

# In[ ]:


string1 = 'BIRT'
string2 = 'PMARR'
with open('/Users/KAHANI/Downloads/My-Family-20-Sep-2021-214410223.ged') as f:
	lines = f.readlines()
    
i = 0

def birtbefmarr():

    for line in lines:


        if string1 in line and string2 in lines[i+2]:

                BirthDate = lines[i+1]
                BirthDateSplit = str.split(BirthDate)
                BirthDateSplit[2] = ' '.join(BirthDateSplit[2:])
                FinalBirthDate = BirthDateSplit[2]
                FinalBirthDateList = []
                FinalBirthDateList.append(FinalBirthDate)
                print(lines[i-2])
                #print(FinalBirthDateList)
                print('Birth date:'+FinalBirthDate)
                BirthDateArray = str.split(FinalBirthDate)
                FinalBirthYear = BirthDateArray[2]
                FinalBirthYearList = []
                FinalBirthYearList.append(FinalBirthYear)
                #print(FinalBirthYearList)

                MarriageDate = lines[i+3]
                MarriageDateSplit = str.split(MarriageDate)
                MarriageDateSplit[2] = ' '.join(MarriageDateSplit[2:])
                FinalMarriageDate = MarriageDateSplit[2]
                FinalMarriageDateList = []
                FinalMarriageDateList.append(FinalMarriageDate)
                #print(FinalMarriageDateList)
                print('Marriage date:'+FinalMarriageDate)
                MarriageDateArray = str.split(FinalMarriageDate)
                FinalMarriageYear = MarriageDateArray[2]
                FinalMarriageYearList = []
                FinalMarriageYearList.append(FinalMarriageYear)
                #print(FinalMarriageYearList)
                if FinalBirthYear < FinalMarriageYear and FinalBirthDate != FinalMarriageDate:
                    print('Birth year <  Marriage year')

                else:
                    print('not valid birth year')

        i += 1

