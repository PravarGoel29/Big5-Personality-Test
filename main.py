with open('/Users/pravar/Downloads/Family-4-19-Sep-2021-014639122 (2).ged') as f:
	lines = f.readlines()

for inputLine in lines:
	print('-->'+inputLine)
	inputLineSplit = str.split(inputLine)

	if(inputLineSplit[0]=='0' and inputLineSplit[1]=='NOTE'):
		inputLineSplit[2]=' '.join(inputLineSplit[2:])
		NoteStatement = inputLineSplit[0]+'|'+inputLineSplit[1]
		if(inputLineSplit[1]=='INDI' or inputLineSplit[1]=='NAME' or inputLineSplit[1]=='SEX' or inputLineSplit[1]=='BIRT' or inputLineSplit[1]=='DEAT' or inputLineSplit[1]=='FAMC' or inputLineSplit[1]=='FAMS' or inputLineSplit[1]=='FAM' or inputLineSplit[1]=='MARR' or inputLineSplit[1]=='HUSB' or inputLineSplit[1]=='WIFE' or inputLineSplit[1]=='CHIL' or inputLineSplit[1]=='DIV' or inputLineSplit[1]=='DATE' or inputLineSplit[1]=='HEAD' or inputLineSplit[1]=='TRLR' or inputLineSplit[1]=='NOTE'):
			print('<--'+NoteStatement+'|Y|'+inputLineSplit[2])
		else:
			print('<--'+NoteStatement + '|N|' + inputLineSplit[2])


	elif(inputLineSplit[0]=='0' and inputLineSplit[1]!='NOTE'):
		IdStatement = inputLineSplit[0]+'|'+inputLineSplit[2]
		if (inputLineSplit[2] == 'INDI' or inputLineSplit[2] == 'NAME' or inputLineSplit[2] == 'SEX' or inputLineSplit[
			2] == 'BIRT' or inputLineSplit[2] == 'DEAT' or inputLineSplit[2] == 'FAMC' or inputLineSplit[2] == 'FAMS' or
				inputLineSplit[2] == 'FAM' or inputLineSplit[2] == 'MARR' or inputLineSplit[2] == 'HUSB' or
				inputLineSplit[2] == 'WIFE' or inputLineSplit[2] == 'CHIL' or inputLineSplit[2] == 'DIV' or
				inputLineSplit[2] == 'DATE' or inputLineSplit[2] == 'HEAD' or inputLineSplit[2] == 'TRLR' or
				inputLineSplit[2] == 'NOTE'):
			print('<--'+IdStatement + '|Y|' + inputLineSplit[1])
		else:
			print('<--'+IdStatement + '|N|' + inputLineSplit[1])


	elif(inputLineSplit[0]=='1' and inputLineSplit[1]=='NAME'):
		inputLineSplit[2] = ' '.join(inputLineSplit[2:])
		Namestatement = inputLineSplit[0]+'|'+inputLineSplit[1]
		if (inputLineSplit[1] == 'INDI' or inputLineSplit[1] == 'NAME' or inputLineSplit[1] == 'SEX' or inputLineSplit[
			1] == 'BIRT' or inputLineSplit[1] == 'DEAT' or inputLineSplit[1] == 'FAMC' or inputLineSplit[1] == 'FAMS' or
				inputLineSplit[1] == 'FAM' or inputLineSplit[1] == 'MARR' or inputLineSplit[1] == 'HUSB' or
				inputLineSplit[1] == 'WIFE' or inputLineSplit[1] == 'CHIL' or inputLineSplit[1] == 'DIV' or
				inputLineSplit[1] == 'DATE' or inputLineSplit[1] == 'HEAD' or inputLineSplit[1] == 'TRLR' or
				inputLineSplit[1] == 'NOTE'):
			print('<--'+Namestatement + '|Y|' + inputLineSplit[2])
		else:
			print('<--'+Namestatement + '|N|' + inputLineSplit[2])


	elif(inputLineSplit[0]=='1' and inputLineSplit[1]=='SEX'):
		SexStatement = inputLineSplit[0]+'|'+inputLineSplit[1]
		print('<--'+SexStatement + '|Y|' + inputLineSplit[2])


	elif(inputLineSplit[0]=='1' and inputLineSplit[1]=='BIRT' or inputLineSplit[1]=='DEAT'):
		BirthDeathStatement = inputLineSplit[0]+'|'+inputLineSplit[1]+'|Y'
		print('<--'+BirthDeathStatement)


	elif(inputLineSplit[0]=='2' and inputLineSplit[1]=='DATE'):
		inputLineSplit[2] = ' '.join(inputLineSplit[2:])
		DateStatement = inputLineSplit[0]+'|'+inputLineSplit[1]
		if (inputLineSplit[1] == 'INDI' or inputLineSplit[1] == 'NAME' or inputLineSplit[1] == 'SEX' or inputLineSplit[
			1] == 'BIRT' or inputLineSplit[1] == 'DEAT' or inputLineSplit[1] == 'FAMC' or inputLineSplit[1] == 'FAMS' or
				inputLineSplit[1] == 'FAM' or inputLineSplit[1] == 'MARR' or inputLineSplit[1] == 'HUSB' or
				inputLineSplit[1] == 'WIFE' or inputLineSplit[1] == 'CHIL' or inputLineSplit[1] == 'DIV' or
				inputLineSplit[1] == 'DATE' or inputLineSplit[1] == 'HEAD' or inputLineSplit[1] == 'TRLR' or
				inputLineSplit[1] == 'NOTE'):
			print('<--'+DateStatement + '|Y|' + inputLineSplit[2])
		else:
			print('<--'+DateStatement + '|N|' + inputLineSplit[2])


	elif (inputLineSplit[0] == '2'):
		Level2Statement = inputLineSplit[0] + '|' + inputLineSplit[1]
		inputLineSplit[2] = ' '.join(inputLineSplit[2:])
		if (inputLineSplit[1] == 'INDI' or inputLineSplit[1] == 'NAME' or inputLineSplit[1] == 'SEX' or inputLineSplit[
			1] == 'BIRT' or inputLineSplit[1] == 'DEAT' or inputLineSplit[1] == 'FAMC' or inputLineSplit[1] == 'FAMS' or
				inputLineSplit[1] == 'FAM' or inputLineSplit[1] == 'MARR' or inputLineSplit[1] == 'HUSB' or
				inputLineSplit[1] == 'WIFE' or inputLineSplit[1] == 'CHIL' or inputLineSplit[1] == 'DIV' or
				inputLineSplit[1] == 'DATE' or inputLineSplit[1] == 'HEAD' or inputLineSplit[1] == 'TRLR' or
				inputLineSplit[1] == 'NOTE'):
			print('<--' + Level2Statement + '|Y|' + inputLineSplit[2])
		else:
			print('<--' + Level2Statement + '|N|' + inputLineSplit[2])


	elif(inputLineSplit[0]=='1' and inputLineSplit[1]=='FAMS' or inputLineSplit[1]=='FAMC'):
		FamilySCStatement = inputLineSplit[0]+'|'+inputLineSplit[1]
		print('<--'+FamilySCStatement + '|Y|' + inputLineSplit[2])


	elif(inputLineSplit[0]=='1' and inputLineSplit[1]=='HUSB' or inputLineSplit[1]=='WIFE' or inputLineSplit[1]=='CHIL' or inputLineSplit[1]=='DIV'):
		HWCDstatement = inputLineSplit[0]+'|'+inputLineSplit[1]+'|Y|'+inputLineSplit[2]
		print('<--'+HWCDstatement)


	elif(inputLineSplit[0]=='1' and inputLineSplit[1]=='MARR'):
		MarrStatement = inputLineSplit[0]+'|'+inputLineSplit[1]+'|Y'
		print('<--'+MarrStatement)


	elif(inputLineSplit[0]!='0' and inputLineSplit[1] != 'INDI' or inputLineSplit[1] != 'NAME' or inputLineSplit[1] != 'SEX' or inputLineSplit[
			1] != 'BIRT' or inputLineSplit[1] != 'DEAT' or inputLineSplit[1] != 'FAMC' or inputLineSplit[1] != 'FAMS' or
				inputLineSplit[1] != 'FAM' or inputLineSplit[1] != 'MARR' or inputLineSplit[1] != 'HUSB' or
				inputLineSplit[1] != 'WIFE' or inputLineSplit[1] != 'CHIL' or inputLineSplit[1] != 'DIV' or
				inputLineSplit[1] != 'DATE' or inputLineSplit[1] != 'HEAD' or inputLineSplit[1] != 'TRLR' or
				inputLineSplit[1] != 'NOTE'):
		if(len(inputLineSplit) == 2):
			print('<--'+inputLineSplit[0]+'|'+inputLineSplit[1]+'|N')
		else:
			inputLineSplit[2] = ' '.join(inputLineSplit[2:])
			inputLineSplit[2] = '|'+inputLineSplit[2]
			print('<--' + inputLineSplit[0] + '|' + inputLineSplit[1] + '|N'+inputLineSplit[2])







