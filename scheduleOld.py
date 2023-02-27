# Victoria Parry 
# Samee Rauf
# CPSC 335 - Project 1
# Algorithm 2 

def PossibleMeetings(person1_Schedule, person1_DailyAct, person2_Schedule, person2_DailyAct, minDuration):
   # removing colons from schedules and daily acts
   person1_DailyAct[0] = person1_DailyAct[0].replace(':','')
   person1_DailyAct[1] = person1_DailyAct[1].replace(':','')
   person2_DailyAct[0] = person2_DailyAct[0].replace(':','')
   person2_DailyAct[1] = person2_DailyAct[1].replace(':','')
   
   for s in person1_Schedule:
      s[0] = s[0].replace(":", "")
      s[1] = s[1].replace(":", "")

   for s in person2_Schedule:
      s[0] = s[0].replace(":", "")
      s[1] = s[1].replace(":", "")

   # converting strings to ints in new array
   int_Sched_1 = [[int(a), int(b)] for a, b in person1_Schedule]
   int_Sched_2 = [[int(a), int(b)] for a, b in person2_Schedule]

   combined_array = int_Sched_1 + int_Sched_2
   
   # sorts new array
   combined_array.sort()
   # print(combined_array)

   # finds limiting start and end time from daily acts
   startTime = max(int(person1_DailyAct[0]), int(person2_DailyAct[0]))
   finTime = min(int(person1_DailyAct[1]), int(person2_DailyAct[1]))

   # find the possible meeting windows and add to new list
   available_times = []
   j = 1
   for i in range(len(combined_array) - 1):

      diff = combined_array[j][0] - combined_array[i][1]

      # double check the and part
      if diff > 0 and combined_array[i][1] > startTime:
         if (combined_array[j][0] - combined_array[i][1]):
            available_times.append([combined_array[i][1], combined_array[j][0]])
      j += 1

   lastTime = max(combined_array[-1][1], combined_array[-2][1])
   # print(lastTime)

   if lastTime < finTime:
      available_times.append([lastTime, finTime])

   # removes times shorter than meeting duration
   for i in available_times:
      if (i[1] - i[0]) < minDuration:
         available_times.remove(i)

   # print(available_times)

   # converts ints to str
   for i in available_times:
      i[0] = str(i[0])
      i[1] = str(i[1])

   finalArray = [[a[:-2] + ":" + a[-2:], b[:-2] + ":" + b[-2:]] for a, b in available_times]

   # finalArray = []
   # for i in range(len(available_times)):
   #    finalArray.append([available_times[i][0][:-2] + ":" + available_times[i][0][-2:], available_times[i][1][:-2] + ":" + available_times[i][1][-2:]])

   # print(finalArray)
   return finalArray


p1_S = [['7:00','8:30'], ['12:00','13:00'], ['16:00','18:00'] ]
p1_D = ['9:00','19:00']

p2_S = [['9:00','10:30'], ['12:20','14:30'], ['14:00','15:00'], ['16:00', '17:00'] ]
p2_D = ['10:00','18:30']

duration = 30

print(PossibleMeetings(p1_S, p1_D, p2_S, p2_D, duration))
