import unittest
import DeathBfDivorce

class TestProject3(unittest.TestCase):

    def test_BirtDate_ne_DeathDate(self):
        FinalDeathDateList, FinalDeathYearList, FinalDivDateList, FinalDivYearList, FinalIndiCode = DeathBfDivorce.DivDeathDate('DEAT','Divorce Date','Death Date')
        for i in range(len(FinalDivDateList)):
            self.assertNotEqual(FinalDivDateList[i], FinalDeathDateList[i])


    def test_BirthYear_less_DeathYear(self):
        FinalDeathDateList, FinalDeathYearList, FinalDivDateList, FinalDivYearList, FinalIndiCode = DeathBfDivorce.DivDeathDate('DEAT','Divorce Date','Death Date')
        for j in range(len(FinalDivDateList)):
            self.assertLessEqual(FinalDivYearList[j],FinalDeathYearList[j])


    def test_DeathYear_more_BirthYear(self):
        FinalDeathDateList, FinalDeathYearList, FinalDivDateList, FinalDivYearList, FinalIndiCode = DeathBfDivorce.DivDeathDate('DEAT','Divorce Date','Death Date')
        for k in range(len(FinalDivDateList)):
            self.assertGreaterEqual(FinalDeathYearList[k],FinalDivYearList[k])


    def test_BirtDate_ns_DeathDate(self):
        FinalDeathDateList, FinalDeathYearList, FinalDivDateList, FinalDivYearList, FinalIndiCode = DeathBfDivorce.DivDeathDate('DEAT','Divorce Date','Death Date')
        for l in range(len(FinalDivDateList)):
            self.assertIsNot(FinalDivDateList[l],FinalDeathDateList[l])


    def test_BirthDate_DeathDate(self):
        FinalDeathDateList, FinalDeathYearList, FinalDivDateList, FinalDivYearList, FinalIndiCode = DeathBfDivorce.DivDeathDate('DEAT','Divorce Date','Death Date')
        for m in range(len(FinalDivDateList)):
            self.assertIsNotNone(FinalDivDateList[m])


    def test_BirthDate_notin_DeathDate(self):
        FinalDeathDateList, FinalDeathYearList, FinalDivDateList, FinalDivYearList, FinalIndiCode = DeathBfDivorce.DivDeathDate('DEAT','Divorce Date','Death Date')
        for n in range(len(FinalDivDateList)):
            self.assertNotIn(FinalDivDateList[n],FinalDeathDateList[n])

