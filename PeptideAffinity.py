peptideList = []
with open('data.txt') as f:
    for line in f:
        words = line.strip("\n").split(" ")
        peptideList.append([words[0], words[1]])
def checkIfPosition5IsQ():
    bind = 0
    notBind = 0
    for peptide in peptideList:
        if(peptide[0] == '1' and peptide[1][4] == 'Q'):
            bind += 1
            print(peptide)
        elif(peptide[0] == '0' and peptide[1][4] == 'Q'):
            notBind += 1
            print(peptide)
    print("bind: " + str(bind))
    print("not bind: " + str(notBind))
# checkIfPosition5IsQ()

def findTheLongestPeptide():
    longest = len(peptideList[0][1])
    for peptide in peptideList:
        if(len(peptide[1]) > longest):
            longest = len(peptide[1])
    print('the longest length is: ' + str(longest))

# findTheLongestPeptide()

aa = ['W','F','A', 'R', 'N', 'D', 'C', 'Q', 'E','G', 'I', 'L', 'M', 'H', 'P', 'S', 'T', 'Y', 'V', 'K']
def checkFirstChar(first):
    bind = 0
    notBind = 0
    for peptide in peptideList:
        if(peptide[0] == '1' and peptide[1][0] == first):
            bind += 1
        elif(peptide[0] == '0' and peptide[1][0] == first):
            notBind += 1
    print(first + " bind: " + str(bind))
    print(first + " not bind: " + str(notBind))
# for peptide in aa:
#     checkFirstChar(peptide)

def checkLastChar(first):
    bind = 0
    notBind = 0
    for peptide in peptideList:
        lastIndex = len(peptide[1]) - 1
        if(peptide[0] == '1' and peptide[1][lastIndex] == first):
            bind += 1
        elif(peptide[0] == '0' and peptide[1][lastIndex] == first):
            notBind += 1
    print(first + " bind: " + str(bind))
    print(first + " not bind: " + str(notBind))
# for peptide in aa:
#     checkLastChar(peptide)

def printFormattedNumber(num, pos):
    if(pos < 29):
        if(num<10):
            print(str(num), end="   ")
        elif(num>99):
            print(str(num), end=" ")
        else:
            print(str(num), end="  ")
    else:
        print(str(num), end='\n')

def checkFrequency(amino, ifBind, positionNumber):
    bind = 0
    for peptide in peptideList:
        if(positionNumber < len(peptide[1])):
            if(peptide[0] == ifBind and peptide[1][positionNumber] == amino):
                bind += 1
    printFormattedNumber(bind, positionNumber)

def createFrequencyChart():
    print(' ', end=": ")
    for i in range(30):
        printFormattedNumber(i+1, i) 
    for peptide in aa:
        print(peptide, end=": ")
        for x in range(30):
            checkFrequency(peptide, '1', x)

def checkPattern():
    bind = 0
    notBind = 0
    for peptide in peptideList:
        if(peptide[1][0] == 'Q'or'A'or'P' 
        and peptide[1][1] == 'Q' or 'A' or 'P' or 'L' or 'C' or 'V' or 'F' or 'K' or 'H' 
        and peptide[1][5] == 'L' or 'V' or 'E'
        and peptide[1][8] == 'I' or 'L'):
            if(peptide[0] == '0'):
                notBind += 1
            else:
                bind += 1
    print("binding: " + str(bind))
    print( "not binding: " + str(notBind))
# checkPattern()

bindingList = []
notBindingList = []
for peptide in peptideList:
        if(peptide[0] == '1'):
            bindingList.append(peptide[1])
        elif(peptide[0] == '0'):
            notBindingList.append(peptide[1])
def calculateAAInPeptide(list):
    highest = ['',0]
    for value in aa:
        rate = 0
        for peptide in list:
            if(peptide.find(value) > 0):
                rate += 1
        if(rate > highest[1]):
            highest = [value, rate]
    print('highest: ',highest)
# calculateAAInPeptide(bindingList)
aaaa = []
for i in aa:
    for j in aa:
        aaaa.append(i+j)

def findCharInPeptide():
    highest = ['',0]
    for value in aaaa:
        count = 0
        rate = 0
        for peptide in bindingList:
            if(peptide.find(value) > 0):
                count += 1
        rate = count/566
        count = 0
        for peptide in notBindingList:
            if(peptide.find(value) > 0):
                count += 1
        rate = rate - (count/962)
        if(count > highest[1]):
            highest = [value, rate]
    print('highest: ',highest)
findCharInPeptide()
