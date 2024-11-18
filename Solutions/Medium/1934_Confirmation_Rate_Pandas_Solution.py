#Pandas Solution
#Step 1: Merge signups and confirmations on user_id using a left join
#Step 2 : use .fillna(0) method to fill NaN values
#Step 3: Filter only the confirmed messages then group by user_id and then count the occurrences
#Step 4: Group by user_id and count all messages (df_total).
#Step 5: Merge df_total and df_confirmations to combine total and confirmed messages.
