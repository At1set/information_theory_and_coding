# Бацюра Илья, Вариант №43
from random import randint, uniform
from math import log2
from pandas import DataFrame


message_count = 19
exp_count = 10


def generateMessages(message_count : int): # P(X)
  messages = []
  chance_sum = 1
  remainder = chance_sum / message_count

  for _ in range(message_count-1):
    message = remainder + (randint(-4000, 4000)*remainder*1e-5) * chance_sum

    chance_sum -= message
    messages.append(message)
  
  message = chance_sum
  messages.append(message)

  return messages


def transitionMatrix(): # P(X / Y)
  matrix = [[0]*message_count for _ in range(message_count)] # Создание нулевой квадратной матрицы.
  y = 0
  for i in range(message_count):
    chance_sum = 1
    y = randint(70, 90) / 100
    chance_sum -= y
    matrix[i][i] = y
    remainder = chance_sum / (message_count-1)
    for j in range(message_count):
      if i == j: continue
      y = uniform(0, remainder * 2) * chance_sum
      chance_sum -= y
      matrix[i][j] = y
    matrix[i][message_count-1] += chance_sum
  
  return matrix


def calculateOutputProbabilitys(p_x, transition_m): # P(Y)
  res = [0]*message_count
  for i in range(message_count):
    for j in range(message_count):
      res[i] +=  p_x[j] * transition_m[j][i]
  
  return res


def inputAndOutputProbability(p_y, transition_m): # P(X, Y)
  res = []
  for i in range(message_count):
    row = []
    for j in range(message_count):
      row.append(p_y[j] * transition_m[j][i])
    res.append(row)
  return res


def conditional_entropy(transition_m, joint_probabilities_m): # H(X / Y)
  res = 0
  for i in range(0, message_count):
    for j in range(0, message_count):
      res += joint_probabilities_m[i][j] * log2(transition_m[i][j])
  return -res


def entropia(p_x): # H(X)
  result = 0
  for i in range(message_count):
    result += p_x[i] * log2(p_x[i])
  return -result


def meanInfAmount(H_X, CONDITIONAL_H): # I(X, Y)
  return H_X - CONDITIONAL_H


def round2print(n, isMatrix=True, ndigits=7):
  res = []
  if not isMatrix:
    for i in range(message_count):
      res.append(round(n[i], ndigits))
    return res
  else:
    for i in range(message_count):
      row = []
      for j in range(message_count):
        row.append(round(n[i][j], ndigits))
      res.append(row)
  return res


def main():
  generalInfAmount = 0

  for i in range(exp_count):
    print("====================================================================================")
    print(f"Эксперимент №{i+1}: \n")

    p_x = generateMessages(message_count) # P(X)
    print(f"P(X): {round2print(p_x, False)} \n")

    transition_M = transitionMatrix() # P(X / Y)
    print(f"P(X / Y): ")
    print(f"{DataFrame(round2print(transition_M))} \n")

    p_y = calculateOutputProbabilitys(p_x, transition_M) # P(Y)
    print(f"P(Y): {round2print(p_y, False)} \n")

    p_xy = inputAndOutputProbability(p_y, transition_M) # P(X, Y)
    print(f"P(X, Y): ")
    print(f"{DataFrame(round2print(p_xy))} \n")

    entrop = entropia(p_x) # H(X)
    print(f"H(X): {round(entrop, 7)}\n")

    entrop_xy = conditional_entropy(transition_M, p_xy) # H(X / Y)
    print(f"H(X / Y): {round(entrop_xy, 7)}\n")

    mean_inf = meanInfAmount(entrop, entrop_xy) # I(X, Y)
    print(f"I(X, Y): {round(mean_inf, 7)}\n")

    generalInfAmount += mean_inf
    print("====================================================================================\n\n")
  
  return print(f"Среднее кол-во информации по всем экспериментам({exp_count}): {round(generalInfAmount/exp_count, 7)}")


if __name__ == "__main__":
  main()