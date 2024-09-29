class Message:
  def __init__(self) -> None:
    self.Chance : float = None
  
  def getStrChance(self, ndigits : int):
    chance = (str(round(self.Chance, ndigits))+"0"*ndigits)[:ndigits+2]
    if chance.count("0") == len(chance)-1: chance = str(self.Chance)
    return chance