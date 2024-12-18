# Бацюра Илья Вариант №43
from Message import Message
from random import randint

from typing import List
import math


expCount = 8
N = 50


def generateMessages(message_count : int) -> List[Message]:
  messages = []
  chance_sum = 1

  for _ in range(message_count-1):
    message = Message()
    message.Chance = randint(1, int(100/4)) / 100 * chance_sum

    chance_sum -= message.Chance
    messages.append(message)
  
  message = Message()
  message.Chance = chance_sum
  messages.append(message)

  return messages


def entropia(messages : List[Message]):
  result = 0
  for message in messages:
    result += message.Chance * math.log2(message.Chance)
  return -result


def maxEntropia(N : int):
  return math.log2(N)


def main():
  generalInfCount = 0

  for i in range(1, expCount+1):
    print(f"Эксперимент №{i}")
    messages = generateMessages(N)
    print(f"Вероятности сгенерированных сообщений: {[message.getStrChance(5) for message in messages]}")
    print(f"Среднее количество информации в совокупности сообщений: {round(entropia(messages), 7)}")
    generalInfCount += entropia(messages)
    print("\n")
  generalInfCount /= expCount

  print(f"\nМаксимальная энтропия в ходе проведенных численных экспериментов: {round(maxEntropia(N), 7)}")
  print(f"Cреднее количество информации по экспериментам: {round(generalInfCount, 7)}")


if __name__ == "__main__":
  main()