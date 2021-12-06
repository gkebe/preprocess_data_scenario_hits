#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 13:27:06 2021

@author: gaoussoukebe
"""

import pandas as pd
from collections import Counter
from itertools import compress
import csv
import glob

dem_list = []
for filepath in glob.iglob('./Batch*.csv'):
    dem_list.append(pd.read_csv(filepath))
dem_info = pd.concat(dem_list)

#dem_info = dem_info[dem_info['Answer.spokenActionDescription.on'] & dem_info['Answer.spokenGoalDescription.on']  & dem_info['Answer.spokenReasoningDescription.on']]

black = dem_info[dem_info["Answer.race_black.on"]]
asian = dem_info[dem_info["Answer.race_asian.on"]]
white = dem_info[dem_info["Answer.race_white.on"]]
native = dem_info[dem_info["Answer.race_USNative.on"]]
pacific_islander = dem_info[dem_info["Answer.race_pacificIslander.on"]]

race_groups = ["Black", "Asian", "White", "Native American", "Pacific Islander"]
race_groups_survey = ["Answer.race_black.on", "Answer.race_asian.on", "Answer.race_white.on", "Answer.race_USNative.on", "Answer.race_pacificIslander.on"]

hispanic = dem_info[dem_info["Answer.ethnicityYes.on"]]
ethnicity_goups = ["Hispanic"]
ethnicity_goups_survey = ["Answer.ethnicityYes.on"]

women = dem_info[dem_info["Answer.genderFemale.on"]]
men = dem_info[dem_info["Answer.genderMale.on"]]
nonbinary = dem_info[dem_info["Answer.genderNonbinary.on"]]
othergender = dem_info[dem_info["Answer.genderOther.on"]]
privategender = dem_info[dem_info["Answer.genderPrivate.on"]]

gender_groups = ["Female", "Male", "Non-binary", "Other", "Private"]
gender_groups_survey = ["Answer.genderFemale.on", "Answer.genderMale.on", "Answer.genderNonbinary.on", "Answer.genderOther.on", "Answer.genderPrivate.on"]

age_35_49 = dem_info[dem_info["Answer.age-Group.ageEarlyMiddle"]]
age_65_ = dem_info[dem_info["Answer.age-Group.ageElder"]]
age_50_64 = dem_info[dem_info["Answer.age-Group.ageLateMiddle"]]
privateage = dem_info[dem_info["Answer.age-Group.agePrivate"]]
age_18_34 = dem_info[dem_info["Answer.age-Group.ageYoung"]]

age_groups = ["18-34", "35-49", "50-64", "65+", "Private"]
age_groups_survey = ["Answer.age-Group.ageYoung", "Answer.age-Group.ageEarlyMiddle", "Answer.age-Group.ageLateMiddle", "Answer.age-Group.ageElder", "Answer.age-Group.agePrivate"]

firstlanguage = Counter([str.lower(i) for i in dem_info["Answer.firstLanguage"].tolist()])

new_csv_dict = {}
for index, row in dem_info.iterrows():
   new_csv_dict[row["WorkerId"]] = {"First Language" : row["Answer.firstLanguage"], "Race":",".join(list(compress(race_groups, row[race_groups_survey].tolist()))), "Hispanic":["No", "Yes"][row["Answer.ethnicityYes.on"]], "Gender":",".join(list(compress(gender_groups, row[gender_groups_survey].tolist()))), "Age":",".join(list(compress(age_groups, row[age_groups_survey].tolist())))}

new_csv_df = pd.DataFrame.from_dict(new_csv_dict).T
new_csv_df.index.name = "Worker ID"

csvfilename = "demographic_information.csv"
new_csv_df.to_csv(csvfilename)

with open(csvfilename, "r") as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)
    row = 0
    for dem_type, groups, survey_groups in [("Race", race_groups, race_groups_survey), ("Ethnicity", ethnicity_goups, ethnicity_goups_survey), ("Gender", gender_groups, gender_groups_survey), ("Age", age_groups, age_groups_survey)]:
        print(f"{dem_type}")
        rows[row] += ["", f"{dem_type}"]
        row += 1
        for i in range(len(groups)):
            print(f"{groups[i]}: {len(dem_info[dem_info[survey_groups[i]]])}")    
            rows[row] += ["", f"{groups[i]}: {len(dem_info[dem_info[survey_groups[i]]])}"]
            row += 1
        print()
        rows[row] += ["", ""]
        row += 1
with open(csvfilename, "w") as csvfile:
    writer = csv.writer(csvfile, lineterminator='\n')
    writer.writerows(rows)
