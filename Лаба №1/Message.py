class Message:
  def __init__(self) -> None:
    self.Chance : float = None
  
  def getStrChance(self, ndigits : int):
    return round(self.Chance, ndigits)