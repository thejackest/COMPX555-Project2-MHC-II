class Peptide:
  def __init__(self, aminoAcid, isBinding):
    self.aminoAcid = aminoAcid
    self.isBinding = isBinding


with open('data.txt') as f:
    for line in f:
        print(line)


