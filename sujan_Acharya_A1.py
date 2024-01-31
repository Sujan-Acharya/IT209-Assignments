#   Author: Sujan Acharya Purpose: To display the list of states and their capitals and population LA1 01/23/2024
def loadItem():
    fname = "stateinfo7.txt"
    f = open(fname, 'r')
    lines = f.readlines()
    slist = []
    for s in lines:
        x = s.split(';')
        x[1] = x[1].strip()
        x[2] = x[2].strip()
        x[3] = x[3].strip()
        slist.append(x)
    return slist


stateList = loadItem()


def displayItems(stateList):
    print("{:<10}{:<25}{:<20}{:<10}".format(
        "Abbv", "State", "Capital", "Population"))
    print("{:<10}{:<25}{:<20}{:<10}".format(
        "====", "======", "========", "=========="))
    print('')
    for s in stateList:
        print("{:<10}{:<25}{:<20}{:<10}".format(s[0], s[1], s[2], s[3]))

def createDict(stateList):
    stateDict = {}
    for s in stateList:
        stateDict[s[0]] = s[1:]
    return stateDict

def outputFile(stateDict):
    with open('output.txt', 'w') as f:
        for key, value in stateDict.items():
            f.write(f'{value[0]},{value[1]},{value[2]}\n')

stateDict = createDict(stateList)
outputFile(stateDict)
    