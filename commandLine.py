#Command line implementation
import random
import csv
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def printList(list):
    print(Back.MAGENTA+"\nYour activity list:")
    for i in range(len(list)):
        print(Back.MAGENTA+str(i+1)+". " + str(list[i][0]) + ": " + str(list[i][1]) + " minutes")

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

print(Fore.GREEN +Style.BRIGHT+ "WELCOME TO MERGER")

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
    print(Fore.RED+"\n\nType out the different activities you have in a day in order(use '_' instead of ' '), and the time it takes to complete in minutes with a space. To finish, type DONE")
    while newactivity.lower() != "done":
        newactivity = input("\nEnter activity + time: ")
        if newactivity.lower() != "done":
            activityList.append(newactivity.split(" "))
            try:
                activityList[-1][1] = int(activityList[-1][1])
            except:
                try:
                    activityList[-1][1] = float(activityList[-1][1])
                except:
                    pass
else:
    CSVPathOption = input(Fore.YELLOW +Style.BRIGHT+ "\nDo you want to use a nonstandard path for your csv?(y/n): ")
    if CSVPathOption.lower() == "y":
        CSVPath = input("\nType the absolute path here(without quotes): ")
    activityList = readCSV(CSVPath)
    
#make sure no activity is a length of 1
for row in activityList:
    if len(row) != 2:
        activityList.remove(row)

#Merging activities
stillMerging = True
totalSavedTime = 0
print(Fore.LIGHTBLUE_EX + "\nHere are the activities to be merged and save time")
while stillMerging:
    if len(activityList) > 1:
        activity1 = random.randint(0, len(activityList)-2)
        activity2 = activity1+1
        print("\nActivity 1:",activityList[activity1][0])
        print("Activity 2:",activityList[activity2][0])
        print("You could save", min(activityList[activity1][1],activityList[activity2][1]), "minutes!")
        mergeDecision = input(Fore.YELLOW+"Do you want to merge activities?(y/n): ")
        if mergeDecision.lower() == "y":
            totalSavedTime += min(activityList[activity1][1],activityList[activity2][1])
            # activity
            activityList[activity1][0] = activityList[activity1][0] + " + " +activityList[activity2][0]
            activityList[activity1][1] = max(activityList[activity1][1],activityList[activity2][1])
            activityList.pop(activity2)
            printList(activityList)
            if len(activityList) == 1:
                stillMerging = False
                print("\nYou have already merged everything together!\n")
                
        else:
            if input("Do you wan't to stop merging?(y/n): ") == "y":
                printList(activityList)
                stillMerging = False

    else:
        print("\nYou have already merged everything together!\n")
        printList(activityList)
        stillMerging = False
print("In total, you have saved", totalSavedTime, "minute(s)!")

#save as text file
saveToTxtFile = input(Fore.YELLOW +Style.BRIGHT+ "\nDo you want to save your activity list as a text file? (y/n):")
if saveToTxtFile.lower() == "y":
    txtPathOption = input(Fore.YELLOW +Style.BRIGHT+ "Do you want to use a nonstandard path for your text file?(y/n): ")
    if txtPathOption.lower() == "y":
        txtPath = input("\nType the absolute path here(without quotes): ")
    with open(txtPath, "w") as textFile:
        textFile.write("My activity list:")
        for activityNum in range(len(activityList)):
            textFile.write("\n"+(str(activityNum+1)+". "+ str(activityList[activityNum][0]) + ": "+ str(activityList[activityNum][1])+ " minutes"))
        print(Fore.GREEN+Style.NORMAL+"Successfully saved Activity list!")

#save as csv file
saveToCSVFile = input(Fore.YELLOW +Style.BRIGHT+ "\nDo you want to save your activity list data as a csv file? (y/n):")
if saveToCSVFile.lower() == "y":
    CSVPathOption = input(Fore.YELLOW +Style.BRIGHT+ "Do you want to use a nonstandard path for your text file?(y/n): ")
    if CSVPathOption.lower() == "y":
        CSVPath = input("\nType the absolute path here(without quotes): ")
    writeCSV(CSVPath, activityList)
    print(Fore.GREEN+Style.NORMAL+"Successfully saved Activity data!")
    
print(Fore.GREEN+Style.BRIGHT+"\nGoodbye!")
    