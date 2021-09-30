class Peptide:
  def __init__(self, aminoAcid, isBinding):
    self.aminoAcid = aminoAcid
    self.isBinding = isBinding

peptideList = []
with open('data.txt') as f:
    for line in f:
        words = line.strip("\n").split(" ")
        peptideList.append(Peptide(words[0], words[1]))
print(len(peptideList))



