import unittest
import DatesBfCurrent

class TestProject3(unittest.TestCase):

    def test_BirtDate_ne_DeathDate(self):
        FinalYearList, FinalDateList,today = DatesBfCurrent.DivDeathDate()
        for i in range(len(FinalDateList)):
            self.assertNotEqual(FinalDateList[i], today)


    def test_BirthYear_less_DeathYear(self):
        FinalYearList, FinalDateList,today = DatesBfCurrent.DivDeathDate()
        for j in range(len(FinalDateList)):
            self.assertLessEqual(int(FinalDateList[j]),2021)


    def test_DeathYear_more_BirthYear(self):
        FinalYearList, FinalDateList,today = DatesBfCurrent.DivDeathDate()
        for k in range(len(FinalDateList)):
            self.assertGreaterEqual(2021,int(FinalDateList[k]))


    def test_BirtDate_ns_DeathDate(self):
        FinalYearList, FinalDateList,today = DatesBfCurrent.DivDeathDate()
        for l in range(len(FinalDateList)):
            self.assertIsNot(FinalDateList[l],today)


    def test_BirthDate_DeathDate(self):
        FinalYearList, FinalDateList,today = DatesBfCurrent.DivDeathDate()
        for m in range(len(FinalDateList)):
            self.assertIsNotNone(FinalDateList[m])



