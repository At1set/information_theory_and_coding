# Бацюра Илья, Вариант №43
from random import uniform, randint
from math import log2

from pandas import DataFrame

message_count = 50
exp_count = 10


def maxEntropia(N : int): # Максимальная энтропия
  return log2(N)


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


def transitionMatrix(): # P(Y / Z)
  matrix = [[0]*message_count for _ in range(message_count)] # Создание нулевой квадратной матрицы.
  y = 0
  for i in range(message_count):
    chance_sum = 1
    for j in range(message_count):
      if i == j: continue
      y = uniform(1e-5, 1/(2*message_count)) * chance_sum
      chance_sum -= y
      matrix[i][j] = y
    matrix[i][i] = chance_sum
  
  return matrix


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


def generateTime(): # τ
  return [uniform(1e-5, message_count) * 1e-6 for _ in range(message_count)]


def symbolAverageTime(p_y, y_time): # τ'
  res = 0
  for i in range(message_count):
    res += p_y[i]*y_time[i]
  return res


def transferSpeed(entrop_y, symb_time): # I(Y)
  return entrop_y / symb_time


def C(N, symb_time): # Пропускная способность дискретного канала без помех
  return maxEntropia(N) / symb_time


def calculateOutputProbabilitys(p_x, transition_m): # P(Z)
  res = [0]*message_count
  for i in range(message_count):
    for j in range(message_count):
      res[i] +=  p_x[j] * transition_m[j][i]
  
  return res


def meanInfAmount(H_X, CONDITIONAL_H): # I(X, Y)
  return H_X - CONDITIONAL_H


def transferSpeedWithInterference(h_y, h_yz, symb_time): # I(Z, Y)
  return meanInfAmount(h_y, h_yz) / symb_time


def C_withInterference(N, h_yz, symb_time): # Пропуская способность дискретного канала с помехами
  return (maxEntropia(N) - h_yz) / symb_time


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
  general_t = 0
  general_c = 0
  general_t_with_inter = 0
  general_c_with_inter = 0

  for i in range(exp_count):
    print("====================================================================================")
    print(f"Эксперимент №{i+1}: \n")
    
    p_y = generateMessages(message_count) # P(Y)
    print(f"P(Y): {round2print(p_y, False)} \n")

    t_y = generateTime() # Массив длительностей символов
    print(f"Массив длительности каждого символа сообщения (с): {round2print(t_y, False)} \n")

    symb_time = symbolAverageTime(p_y, t_y) # Средняя длительность символов
    h_y = entropia(p_y) # энтропия

    transition_M = transitionMatrix() # P(Y / Z)
    print("P(Y / Z): ")
    print(DataFrame(round2print(transition_M)))
    
    t = transferSpeed(h_y, symb_time)
    c = C(message_count, symb_time)
    print(f"\nСкорость передачи без помех: {round(t, 7)}бит/с")
    print(f"Пропускная способность без помех: {round(c, 7)}бит/с \n")
    
    p_z = calculateOutputProbabilitys(p_y, transition_M) # P(Z)
    p_yz = inputAndOutputProbability(p_z, transition_M)  # P(Y, Z)
    h_yz = conditional_entropy(transition_M, p_yz)       # H(Y / Z)
    
    t_with_inter = transferSpeedWithInterference(h_y, h_yz, symb_time)
    c_with_inter = C_withInterference(message_count, h_yz, symb_time)
    print(f"Скорость передачи с помехами: {round(t_with_inter, 7)}бит/с")
    print(f"Пропускная способность с помехами: {round(c_with_inter, 7)}бит/с\n")
    
    general_t += t
    general_c += c
    general_t_with_inter += t_with_inter
    general_c_with_inter += c_with_inter

    print("====================================================================================\n\n")
  
  print(f"Средняя скорость передачи без помех: {round(general_t / exp_count, 7)}бит/с")
  print(f"Средняя пропускная способность без помех: {round(general_c / exp_count, 7)}бит/с\n")

  print(f"Средняя скорость передачи с помехами: {round(general_t_with_inter / exp_count, 7)}бит/с ")
  print(f"Средняя пропускная способность с помехами: {round(general_c_with_inter / exp_count, 7)}бит/с")


if __name__ == "__main__":
  main()