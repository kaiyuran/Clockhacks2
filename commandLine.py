#Command line implementation
import random


def printList(list):
    print("Your activity list:")
    for i in range(len(list)):
        print(str(i)+".", list[i][0], list[i][1], "minutes")







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



stillMerging = True
while stillMerging:
    activity1 = activityList[random.randint(0, len(activityList)-1)]
    activity2 = activityList[activityList.index(activity1)+1]
    print("Activity 1:",activityList[activity1][0])
    print("Activity 2:",activityList[activity2][0])
    print("You could save", min(activityList[activity1][1],activityList[activity2][1]), " minutes!")
    mergeDecision = input("Do you want to merge activities?(y/n): ")
    if mergeDecision.lower == "y":
        # activity
        pass
    else:
        stillMerging = False