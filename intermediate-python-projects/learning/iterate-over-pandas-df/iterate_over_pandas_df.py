import pandas

student_dict = {
    "student" : ["Eli", "James", "Lily"],
    "score" : [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)

# Loop through a dataframe

# for (key, value) in student_df.items() :
#     print(key)

# Loop through rows of a dataframe

for (index, row) in student_df.iterrows():
    #print(row)
    # print(row.student)
    if row.student == "Eli":
        print(row.score)