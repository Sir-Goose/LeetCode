import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(columns={'id': 'student_id'})
    students = students.rename(columns={'first': 'first_name'})
    students = students.rename(columns={'last': 'last_name'})
    students = students.rename(columns={'age': 'age_in_years'})

    return students
