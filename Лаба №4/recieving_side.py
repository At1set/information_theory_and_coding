import numpy as np
import os


def control_sum(sys_code, H_T, H_2):
  S = np.array([])
  for i in range(H_T.shape[0]):
    Si = 0
    for j in range (H_T.shape[1]):
      if H_T[i][j] == 1:
        Si+= sys_code[j]
    for j in range(H_2.shape[1]):
      if H_2[i][j] == 1:
        Si+= sys_code[j+H_T.shape[1]]
    S = np.append(S, Si%2)
  return S


def get_index_of_mistake(H_T, H_2, S):
  for i in range(H_T.shape[1]):
    a = 0
    for j in range(H_T.shape[0]):
      if (H_T[j][i] == S[j]):
        a+=1
    if a == H_T.shape[0]:
      return (i)
  for i in range(H_2.shape[1]):
    a = 0
    for j in range(H_2.shape[0]):
      if (H_2[j][i] == S[j]):
        a+=1
    if a == H_T.shape[0]:
      return (H_T.shape[1]+i)
  return "Нет ошибки"


def receive(exp_i):
  load_folder = fr"D:\At1set\Учеба\Теория информации и кодирование\Лаба №4\Эксперименты\Эксперимент №{exp_i}"

  load_path_H_T = os.path.join(load_folder, "H_T.npy")
  load_path_H_2 = os.path.join(load_folder, "H_2.npy")
  load_path_sys_code = os.path.join(load_folder, "system_code.npy")

  H_T = np.load(load_path_H_T)
  H_2 = np.load(load_path_H_2)
  sys_code = np.load(load_path_sys_code)
  return H_T, H_2, sys_code


def main(exp_i):
  H_T, H_2, sys_code = receive(exp_i)
  print("Полученный системный код:  ", sys_code)

  S = control_sum(sys_code, H_T, H_2)
  print("Контрольная сумма: ", S)

  N = get_index_of_mistake(H_T, H_2, S)
  print("Индекс элемента с ошибкой: ", N)

  if type(N) == int:
    sys_code[N] = sys_code[N] ^ 1
  print("Исправленный системный код:", sys_code)


if __name__ == "__main__":
  main(1)