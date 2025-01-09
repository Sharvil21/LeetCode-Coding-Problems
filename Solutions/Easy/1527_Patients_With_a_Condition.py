#Solution 1
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients.query("conditions.str.contains('(^|[\s])DIAB1')")
   

#Solution 2 
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients.loc[patients['conditions'].str.contains("(^|[\s])DIAB1")]
    
