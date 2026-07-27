# syntex for (for loop)
#for variable in range(start,stop,step)
# code to repeat
for i in range(0,10,2):
     print(i)

# syntex for (while loop)
#while condition:
# code to repeat
print("\n")
count = 0
while count < 10:
     print(count)
     count += 1

#using time.sleep()for delays
print("\n")
import time
for i in range(5,0,-1):
     time.sleep(1)
     print(i)
print("happy birthday!")

#day 6 project: countdown timer
import time
#step:1 get user input for countdown start
start = int(input("Enter the number to start the countdown from:"))

#step 2:Countdown using while loop
print("\n---Countdown begins---")
while start > 0:
     print(start)
     time.sleep(1)
     start -= 1
#step 3: print message
print("\n---Countdown complete---")