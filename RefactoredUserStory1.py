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




# def convertdate(d):
#        d=d.split(" ")
#        mo=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
#        return datetime.datetime(int(d[2]), mo.index(d[1])+1, int(d[0]))

def marrbeforedeat():
    mo = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

    # Path to your `.ged` file
    file_path = '/Users/pravar/Downloads/Family-4-19-Sep-2021-014639122 (2).ged'
    gedcom_parser = Parser()
    # Parse your file
    gedcom_parser.parse_file(file_path)
    root_child_elements = gedcom_parser.get_root_child_elements()
    # Iterate through all root child element
    for element in root_child_elements:
        if element.get_tag() == "FAM":
            arr = []
            error = 0
            mar_date = "not available"
            # print(element.get_pointer())
            for i in element.get_child_elements():
                if i.get_tag() == "HUSB" or i.get_tag() == "WIFE":
                    arr.append(i.get_value())

            if i.get_tag() == "MARR":
                for k in i.get_child_elements():
                    # print(k)
                    if k.get_tag() == "DATE":
                        mar_date = k.get_value()
                        # mar_date=convertdate(mar_date)
                        mar_date1 = mar_date.split(" ")
                        mar_date2 = datetime.datetime(int(mar_date1[2]), mo.index(mar_date1[1]) + 1, int(mar_date1[0]))
                        print(mar_date1)
            if mar_date2 != "not available":
                for per in root_child_elements:
                    # print(per.get_pointer())
                    if per.get_pointer() in arr:
                        # print(per.get_pointer())
                        for pe in per.get_child_elements():
                            # print(pe)
                            if pe.get_tag() == "DEAT":
                                # print(pe)
                                for p in pe.get_child_elements():
                                    if p.get_tag() == "DATE":
                                        deat_date = p.get_value()
                                        deat_date1 = deat_date.split(" ")
                                        # deat_date=convertdate(deat_date)
                                        deat_date2 = datetime.datetime(int(deat_date1[2]), mo.index(deat_date1[1]) + 1,
                                                                       int(deat_date1[0]))
                                        print(deat_date2)
                                        if deat_date2 < mar_date2:
                                            error = 1

            if (error == 1):
                print("Marriage date invalid for family:" + element.get_pointer())

        # else:
        #     print("marriage date not available")
    # print(error)
    print("End of Program")

