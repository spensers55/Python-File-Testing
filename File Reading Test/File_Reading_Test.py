treeList = []

def readList():
    global treeList
    treeFile = open("testFile.txt")
    fileLine = treeFile.readline()
    readStr = ""
    listIndex = 0
    for i in fileLine:
        if i != "#":
            readStr += i
        else:
            treeList.append(readStr)
            readStr = ""
            listIndex += 1
    treeFile.close()

def addTree(newTree):
    treeList.append(newTree)
    print("Tree type added")

def removeTree(badTree): # stolen from my class testing project
    global treeList
    found = False
    for i in treeList:
        if i == badTree:
            found = True
    if found == False:
        print("Type not found")
    else:
        treeList.remove(badTree)
        print("Type removed")
    print("\n\n")

def saveTrees():
    global treeList
    treeFile = open("testFile.txt", "w")
    for i in treeList:
        treeFile.write(i+"#")
    treeFile.close()

def printTrees():
    global treeList
    print(treeList)

readList()
repeat = True
while repeat:
    print("1: remove\n"+
          "2: add\n"+
          "3: print\n"+
          "4: save/quit\n")
    choice = input("enter choice: ")
    if choice == "4":
        repeat = False
        saveTrees()
    elif choice == "3":
        printTrees()
    elif choice == "2":
        addTree(input("Enter new tree type: "))
    elif choice == "1":
        removeTree(input("Enter tree type to be removed: "))