peptideList = []
with open('data.txt') as f:
    for line in f:
        words = line.strip("\n").split(" ")
        peptideList.append([words[0], words[1]])
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




