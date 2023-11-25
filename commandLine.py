#Command line implementation

print("""
WELCOME TO MERGER
To Start, type out the different activities you have in a day in order, and the time it takes to complete in minutes wiht a space. To finish, type DONE
""")

#initial input
activityList = []
newactivity = ""
while newactivity.lower() != "done":
    newactivity = input("Enter activity + time: ")
    if newactivity.lower() != "done":
        activityList.append(newactivity.split(" "))
        try:
            activityList[-1][1] = int(activityList[-1][1])
        except:
            activityList[-1][1] = float(activityList[-1][1])
        

#print in readable format:

print("Your activity list:")
for i in range(len(activityList)):
    print(str(i)+".", activityList[i][0], activityList[i][1], "minutes")
