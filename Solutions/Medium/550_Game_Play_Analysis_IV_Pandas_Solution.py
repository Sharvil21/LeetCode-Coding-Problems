#Pandas Solution
#First Sort the values by player_id and the event_date just for precaution
#Then create a new column which shows the immediate next login date for each player. Can be done using .shift() method and group by each player_id
#Then create another column which shows the difference between the next login date and the actual event date
