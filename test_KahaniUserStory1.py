#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
import UserStoryCode

class TestProject(unittest.TestCase):

	def test_BirtDate_ne_parMarriageDate(self):
		for i in range(len(UserStoryCode.FinalBirthDateList)):
			self.assertNotEqual(UserStoryCode.FinalBirthDateList[i], UserStoryCode.FinalparMarriageList[i])

	def test_BirthYear_less_parMarriageYear(self):
		for j in range(len(UserStoryCode.FinalBirthYearList)):
			self.assertLessEqual(UserStoryCode.FinalBirthYearList[j], UserStoryCode.FinalparMarriageYearList[j])

	def test_parMarriageYear_more_BirthYear(self):
		for k in range(len(UserStoryCode.FinalBirthYearList)):
			self.assertGreaterEqual(UserStoryCode.FinalparMarriageYearList[k], UserStoryCode.FinalBirthYearList[k])

	def test_BirtDate_ns_parMarriageDate(self):
		for l in range(len(UserStoryCode.FinalBirthYearList)):
			self.assertIsNot(UserStoryCode.FinalBirthDateList[l], UserStoryCode.FinalparMarriageDateList[l])

	def test_BirthDate_parMarriageDate(self):
		for m in range(len(UserStoryCode.FinalBirthYearList)):
			self.assertIsNotNone(UserStoryCode.FinalBirthDateList[m])

	def test_BirthDate_notin_parMarriageDate(self):
		for n in range(len(UserStoryCode.FinalBirthYearList)):
			self.assertNotIn(UserStoryCode.FinalBirthDateList[n], UserStoryCode.FinaparMarriageDateList[n])


# In[ ]:




