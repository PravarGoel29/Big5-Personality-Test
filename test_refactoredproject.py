import unittest
import RefactoredUserStory1

class TestProject2(unittest.TestCase):

    def test_BirtDate_ne_DeathDate(self):
        FinalLDateList, FinalLYearList, FinalGDateList, FinalGYearList = RefactoredUserStory1.BirthDeathDate('BIRT', 'DEAT','Birth Date','Death Date')
        for i in range(len(FinalLDateList)):
            self.assertNotEqual(FinalLDateList[i], FinalGDateList[i])
        FinalLDateList, FinalLYearList, FinalGDateList, FinalGYearList = RefactoredUserStory1.BirthDeathDate('MARR', 'DIV', 'Marriage Date', 'Divorce Date')
        for i in range(len(FinalLDateList)):
            self.assertNotEqual(FinalLDateList[i], FinalGDateList[i])

    def test_BirthYear_less_DeathYear(self):
        FinalLDateList, FinalLYearList, FinalGDateList, FinalGYearList = RefactoredUserStory1.BirthDeathDate('BIRT', 'DEAT','Birth Date','Death Date')
        for j in range(len(FinalLDateList)):
            self.assertLessEqual(FinalLYearList[j],FinalGYearList[j])
        FinalLDateList, FinalLYearList, FinalGDateList, FinalGYearList = RefactoredUserStory1.BirthDeathDate('MARR', 'DIV', 'Marriage Date', 'Divorce Date')
        for j in range(len(FinalLDateList)):
            self.assertLessEqual(FinalLYearList[j], FinalGYearList[j])

    def test_DeathYear_more_BirthYear(self):
        FinalLDateList, FinalLYearList, FinalGDateList, FinalGYearList = RefactoredUserStory1.BirthDeathDate('BIRT', 'DEAT','Birth Date','Death Date')
        for k in range(len(FinalLDateList)):
            self.assertGreaterEqual(FinalGYearList[k],FinalLYearList[k])
        FinalLDateList, FinalLYearList, FinalGDateList, FinalGYearList = RefactoredUserStory1.BirthDeathDate('MARR', 'DIV', 'Marriage Date', 'Divorce Date')
        for k in range(len(FinalLDateList)):
            self.assertGreaterEqual(FinalGYearList[k], FinalLYearList[k])

    def test_BirtDate_ns_DeathDate(self):
        FinalLDateList, FinalLYearList, FinalGDateList, FinalGYearList = RefactoredUserStory1.BirthDeathDate('BIRT', 'DEAT','Birth Date','Death Date')
        for l in range(len(FinalLDateList)):
            self.assertIsNot(FinalLDateList[l],FinalGDateList[l])
        FinalLDateList, FinalLYearList, FinalGDateList, FinalGYearList = RefactoredUserStory1.BirthDeathDate('MARR', 'DIV', 'Marriage Date', 'Divorce Date')
        for l in range(len(FinalLDateList)):
            self.assertIsNot(FinalLDateList[l], FinalGDateList[l])

    def test_BirthDate_DeathDate(self):
        FinalLDateList, FinalLYearList, FinalGDateList, FinalGYearList = RefactoredUserStory1.BirthDeathDate('BIRT', 'DEAT','Birth Date','Death Date')
        for m in range(len(FinalLDateList)):
            self.assertIsNotNone(FinalLDateList[m])
        FinalLDateList, FinalLYearList, FinalGDateList, FinalGYearList = RefactoredUserStory1.BirthDeathDate('MARR', 'DIV', 'Marriage Date', 'Divorce Date')
        for m in range(len(FinalLDateList)):
            self.assertIsNotNone(FinalLDateList[m])

    def test_BirthDate_notin_DeathDate(self):
        FinalLDateList, FinalLYearList, FinalGDateList, FinalGYearList = RefactoredUserStory1.BirthDeathDate('BIRT', 'DEAT','Birth Date','Death Date')
        for n in range(len(FinalLDateList)):
            self.assertNotIn(FinalLDateList[n],FinalGDateList[n])
        FinalLDateList, FinalLYearList, FinalGDateList, FinalGYearList = RefactoredUserStory1.BirthDeathDate('MARR', 'DIV', 'Marriage Date', 'Divorce Date')
        for n in range(len(FinalLDateList)):
            self.assertNotIn(FinalLDateList[n], FinalGDateList[n])
