import unittest
import UserStoryCode

class TestProject(unittest.TestCase):

	def test_BirtDate_ne_DeathDate(self):
		for i in range(len(UserStoryCode.FinalBirthDateList)):
			self.assertNotEqual(UserStoryCode.FinalBirthDateList[i], UserStoryCode.FinalDeathDateList[i])

	def test_BirthYear_less_DeathYear(self):
		for j in range(len(UserStoryCode.FinalBirthYearList)):
			self.assertLessEqual(UserStoryCode.FinalBirthYearList[j], UserStoryCode.FinalDeathYearList[j])

	def test_DeathYear_more_BirthYear(self):
		for k in range(len(UserStoryCode.FinalBirthYearList)):
			self.assertGreaterEqual(UserStoryCode.FinalDeathYearList[k], UserStoryCode.FinalBirthYearList[k])

	def test_BirtDate_ns_DeathDate(self):
		for l in range(len(UserStoryCode.FinalBirthYearList)):
			self.assertIsNot(UserStoryCode.FinalBirthDateList[l], UserStoryCode.FinalDeathDateList[l])

	def test_BirthDate_DeathDate(self):
		for m in range(len(UserStoryCode.FinalBirthYearList)):
			self.assertIsNotNone(UserStoryCode.FinalBirthDateList[m])

	def test_BirthDate_notin_DeathDate(self):
		for n in range(len(UserStoryCode.FinalBirthYearList)):
			self.assertNotIn(UserStoryCode.FinalBirthDateList[n], UserStoryCode.FinalDeathDateList[n])

