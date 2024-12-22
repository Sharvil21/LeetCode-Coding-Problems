#Pandas Solution
#First combine the lat lon columns so its easier to group by.
#Then create another Dataframe where we get only the Unique lat and lon
#Create another dataframe where we get only those tiv_2015 which are duplicates
#Get the corresponding lat_lon values from the 1st df. Then get the corresponding tiv_2015 values from the other df
#Lastly, use the .loc[] in insurance DataFrame, and use in the .isin() method to only filter out those rows which satisfy the condition of the values we get from both the other dataframes we created
#Get the sum, then create the dataframe
#Return the output by creating a new dataframe
import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    insurance['lat_lon'] = insurance['lat'].astype(str) + ' ' + insurance['lon'].astype(str)
    df = insurance.groupby('lat_lon',as_index=False).agg(count=('lat_lon','count'))
    lat_lon_values = df.loc[df['count']==1,'lat_lon']
    df2 = insurance.groupby('tiv_2015',as_index=False).agg(count=('tiv_2015','count'))
    tiv_2015_values= df2.loc[df2['count']>1,'tiv_2015']
    final_df = insurance.loc[(insurance['tiv_2015'].isin(tiv_2015_values)) & (insurance['lat_lon'].isin(lat_lon_values))]
    return pd.DataFrame({'tiv_2016':[final_df['tiv_2016'].sum()]})
