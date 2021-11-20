

def husbandwifegender():

    #userStoryName('US12')
    results = get_family() 
	
    for res in results:
		if ("HUSBAND" or "WIFE") in res:
			#print("___________"+res["HUSBAND"])
			#print("___________"+res["WIFE"])
			husband = res["HUSBAND"]
			wife = res["WIFE"]
			
			#indi = get_people()
			for temp in indi:
				if husband == temp["ID"] and (temp["SEX"] == "F"):
                    
						
					

			
						message = "Gender for Husband ID "+str(husband)+", is F, therefore Gender is not valid."
						save_invalid_people_for_print(temp["ID"], "US12", message)
	
				if wife == temp["ID"] and (temp["SEX"] == "M"):
                    
					
						
					

			
						message = "Gender for Wife ID "+str(wife)+", is M, therefore Gender is not valid."
						#save_invalid_people_for_print(temp["ID"], "US12", message)
	
