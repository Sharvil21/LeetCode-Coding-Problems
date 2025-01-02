#Solution that beats 100%
ages = []
count = 0
for i in details:
  ages.append(i[11:13])

for i in ages:
  if i>60:
    count+=1

return count
