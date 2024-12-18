import random
import numpy as np
import os

k = 19
dmin = 3
def get_N(k):
  n = 0
  k_2 = 2**k
  while True:
    if k_2 <= ((2**n) / (1+n)):
      break
    else:
      n+=1
  return n


def generate_Uk(k):
  matrix = []
  for i in range(k):
    row = [0]*k
    row[i] = 1
    matrix.append(row)
  matrix = np.array(matrix)
  return matrix


def generate_Hp(k, p, dmin):
  matrix = []

  while len(matrix) < k:
    row = np.random.randint(0, dmin-1, p)
    if np.sum(row) < dmin-1:
      continue 
    if any(np.array_equal(row, existing_row) for existing_row in matrix):
      continue  
    if all(np.sum(np.bitwise_xor(row, existing_row)) >= dmin-2 for existing_row in matrix):
      matrix.append(row)  

  matrix = np.array(matrix)
  matrix = matrix[np.lexsort(matrix.T[::-1])]
  
  return matrix


def show_matrixes(Uk, Hp, k):
  for i in range(k):
    print(Uk[i], Hp[i])
  print("\n", end="")


def get_H(Hp):
  H_T = np.transpose(Hp)
  H_2 = []
  for i in range(H_T.shape[0]):
    row = [0]*H_T.shape[0]
    
    row[i] = 1
    H_2.append(row)
  H_2 = np.array(H_2)
  return H_T, H_2


def generate_message(k):
  mas = []
  for i in range (k):
    mas.append(random.randint(0, 1))
  mas = np.array(mas)
  return mas


def get_system_code(H_T, mas, p):
  sys_code = mas
  for j in range (p):
    b = 0
    for i in range (mas.shape[0]):
      if H_T[j][i] == 1:
        b+= mas[i]
    sys_code = np.append(sys_code, b%2)
  return sys_code


def make_mistake(sys_code):
  i = random.randint(0, sys_code.shape[0] - 1)
  sys_code[i] = random.randint(0, 1)


def transmit(exp_i, HpT, H_2, sys_code):
  save_folder = fr"D:\At1set\Учеба\Теория информации и кодирование\Лаба №4\Эксперименты\Эксперимент №{exp_i}"
  os.makedirs(save_folder, exist_ok=True)

  save_path = os.path.join(save_folder, "H_T")
  np.save(save_path, HpT)

  save_path = os.path.join(save_folder, "H_2")
  np.save(save_path, H_2)

  save_path = os.path.join(save_folder, "system_code")
  np.save(save_path, sys_code)


def main(exp_i):
  n = get_N(k)
  p = n - k

  Uk = generate_Uk(k)
  Hp = generate_Hp(k, p, dmin)

  print("Производящая матрица Hp: ")
  show_matrixes(Uk, Hp, k)

  HpT, H_2 = get_H(Hp)

  print("Проверочная матрица H: ")
  show_matrixes(HpT, H_2, HpT.shape[0])

  HpT = np.transpose(Hp)

  message = generate_message(k)
  print("Сообщение:                         ", message)

  sys_code = get_system_code(HpT, message, p)
  print("Систематический код:               ", sys_code)

  make_mistake(sys_code)
  print("Код с возможной ошибкой / без нее: ", sys_code)

  transmit(exp_i, HpT, H_2, sys_code)


if __name__ == "__main__":
  main(1)