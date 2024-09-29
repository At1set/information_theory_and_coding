# Бацюра Илья Вариант №43
from Message import Message
from random import randint


def generateMessages(message_count):
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


expCount = 8
N = 50


messages = generateMessages(N)


# def entropia(messages):
  