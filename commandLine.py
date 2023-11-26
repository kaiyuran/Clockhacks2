#Command line implementation
import random
import csv


def printList(list):
    print("\nYour activity list:")
    for i in range(len(list)):
        print(str(i+1)+".", str(list[i][0]) + ":", list[i][1], "minutes")

def readCSV(filename):
    with open(filename, 'r', newline='') as file:
        lists = csv.reader(file)
        data = list(lists)
        for row in range(len(data)):
            data[row][1] = float(data[row][1])
        return data
def writeCSV(filename, data):
    with open(filename, 'w', newline='') as file:
        lists = csv.writer(file)
        for row in data:
            lists.writerow(row)

        


CSVPath = "./data.csv"
txtPath = "./myActivityList.txt"


print("""WELCOME TO MERGER""")

#Type of input
correctInput = False
while not correctInput:
    typeOfInput = input("To Start, type 1 for inputting the activity list manually and type 2 for inputting from a file: ")
    if (typeOfInput == "1" or typeOfInput == "2"):
        correctInput = True
    else:
        print("Sorry, that is not a valid option, please try again.\n")

if typeOfInput == "1":
    #new list manually
    activityList = []
    newactivity = ""
    print("Type out the different activities you have in a day in order, and the time it takes to complete in minutes wiht a space. To finish, type DONE")
    while newactivity.lower() != "done":
        newactivity = input("Enter activity + time: ")
        if newactivity.lower() != "done":
            activityList.append(newactivity.split(" "))
            try:
                activityList[-1][1] = int(activityList[-1][1])
            except:
                activityList[-1][1] = float(activityList[-1][1])
else:
    CSVPathOption = input("do you want to use a nonstandard path for your csv?(y/n): ")
    if CSVPathOption.lower() == "y":
        CSVPath = input("\nType the absolute path here: ")
    activityList = readCSV(CSVPath)
    

print(activityList)


#Merging activities
stillMerging = True
totalSavedTime = 0
print("Here are the activities to be merged and save time")
while stillMerging:
    activity1 = random.randint(0, len(activityList)-2)
    activity2 = activity1+1
    print("\nActivity 1:",activityList[activity1][0])
    print("Activity 2:",activityList[activity2][0])
    print("You could save", min(activityList[activity1][1],activityList[activity2][1]), "minutes!")
    mergeDecision = input("Do you want to merge activities?(y/n): ")
    if mergeDecision.lower() == "y":
        totalSavedTime += min(activityList[activity1][1],activityList[activity2][1])
        # activity
        activityList[activity1][0] = activityList[activity1][0] + " + " +activityList[activity2][0]
        activityList[activity1][1] = max(activityList[activity1][1],activityList[activity2][1])
        activityList.pop(activity2)
        printList(activityList)
        if len(activityList) == 1:
            stillMerging = False
            print("You have already merged everything together!")
            
    else:
        if input("Do you wan't to stop merging?(y/n): ") == "y":
            printList(activityList)
            stillMerging = False
print("In total, you have saved", totalSavedTime, "minute(s)!")


#save as text file
saveToTxtFile = input("Do you want to save your activity list as a text file? (y/n):")
if saveToTxtFile.lower() == "y":
    txtPathOption = input("Do you want to use a nonstandard path for your text file?(y/n): ")
    if txtPathOption.lower() == "y":
        txtPath = input("\nType the absolute path here: ")
    with open(txtPath, "w") as textFile:
        textFile.write("My activity list:")
        for activityNum in range(len(activityList)):
            textFile.write("\n"+(str(activityNum+1)+". "+ str(activityList[activityNum][0]) + ": "+ str(activityList[activityNum][1])+ " minutes"))
        print("Successfully saved Activity list!")

#save as csv file
saveToCSVFile = input("\nDo you want to save your activity list data as a csv file? (y/n):")
if saveToCSVFile.lower() == "y":
    CSVPathOption = input("Do you want to use a nonstandard path for your text file?(y/n): ")
    if CSVPathOption.lower() == "y":
        CSVPath = input("\nType the absolute path here: ")
    writeCSV(CSVPath, activityList)
    print("Successfully saved Activity data!")
print("\nGoodbye!")
    
    

