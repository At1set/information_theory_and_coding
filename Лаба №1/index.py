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


def printMessageChances(messages : List[Message], ndigits : int):
  sorted_messages : List[Message]
  sorted_messages = sorted(messages, key=lambda x: x.Chance, reverse=True)
  for i, message in enumerate(sorted_messages):
    print(f"Сообщение №{i+1}, шанс: {message.getStrChance(ndigits)}")


def entropia(messages : List[Message]):
  result = 0
  for message in messages:
    result += message.Chance * math.log2(message.Chance)
  return -result


def maxEntropia(N : int):
  return math.log2(N)


def main():
  for i in range(1, expCount+1):
    messages = generateMessages(N)

    print(f"Эксперимент №{i}")
    print(f"Среднее количество информации в совокупности сообщений: {entropia(messages)}")
  
  print(f"\nМаксимальная энтропия в ходе проведенных численных экспериментов: {maxEntropia(N)}")

  choice = input("\nВведите 1 для показа вероятностей сгенерированных сообщений: ")
  if (choice == "1"):
    for message in messages: print(message.getStrChance(5))


if __name__ == "__main__":
  main()