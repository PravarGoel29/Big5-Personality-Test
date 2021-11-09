from datetime import date


def Adityafunction():
    userStoryName('US11')
    results = get_family()
    indi = get_people()
    for res in results:
        if "CHILDREN" in res:
            child = res['CHILDREN']
            childd = list(x for x in indi if x["ID"] in child)
            # print childd
        for sibling in childd:
            sib_fam = next((x for x in results if x["HUSBAND"] == sibling["ID"]), None)
            # print sib_fam
            if sib_fam and sib_fam["WIFE"] in child:
                message = "Sibling is married to another sibling"
                # save_invalid_family_for_print(sib_fam["FAMID"], "US11", message)

