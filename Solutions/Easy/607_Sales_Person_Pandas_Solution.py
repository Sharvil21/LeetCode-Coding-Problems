#Pandas Solution
import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df1 = sales_person.merge(orders,on='sales_id', how = 'left')
    final_df = merged_df1.merge(company,on='com_id',how='left')
    names_to_be_excluded = final_df.loc[final_df['name_y']=='RED','name_x']
    return sales_person.query("name not in @names_to_be_excluded")['name'].to_frame('name')

#Another Pandas Solution
def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return sales_person[
        ~sales_person['sales_id'].isin(
            pd.merge(
                left=orders,
                right=company[company['name'] == 'RED'],
                on='com_id',
                how='inner',
            )['sales_id'].unique()
        )
    ][['name']]

#Third 
