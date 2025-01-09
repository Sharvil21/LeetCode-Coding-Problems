#Solution 1
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients.query("conditions.str.contains('(^|[\s])DIAB1')")
    
