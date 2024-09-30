#Pandas Solution
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher.groupby('teacher_id')['subject_id'].nunique().to_frame('cnt').reset_index()

#Second Pandas Solution (Using .agg() method)
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher.groupby('teacher_id').agg(cnt=('subject_id','nunique')).reset_index()
