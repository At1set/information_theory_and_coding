import numpy as np
import os
import random
import math


k = 50


def get_N(k):
  n = 0
  k_2 = 2**k
  while True:
    if k_2 <= ((2**n) / (1+n)):
      break
    else:
      n+=1
  return n


def generate_message(k):
  result = []
  for _ in range(k):
    result.append(random.randint(0, 1))
  result = np.array(result)
  return result


def hamming_code(k,p,message):
  result = [0]*(k+p)
  
  for i in range(k+p):
    if math.log2(i+1) - int(math.log2(i+1)) != 0 :
      result[i] = message[0]
      message = np.delete(message,0)
    else:
      result[i] = 2
  
  for i in range (p):
    s = 0
    l = i+1
    for j in range(k+p):
      bin_ = format(j+1,"b")
      bin_j = list(bin_)
      try:
        if bin_j[len(bin_j) - l]  == "1" and len(bin_j) - l >= 0:
          s+= result[j]
      except:
        continue
    
    for j in range(k+p):
      if result[j] == 2:
        result[j] = s % 2
        break
  
  return result


def make_mistake(sys_code):
  i = random.randint(0,2)
  for _ in range(i):
    l = random.randint(0,len(sys_code)-1)
    sys_code[l] = sys_code[l] ^ 1
  return sys_code


def transmit(path, hamming, k, p):
  os.makedirs(path, exist_ok=True)

  save_path = os.path.join(path, "hamming")
  np.save(save_path, hamming)  

  save_path = os.path.join(path, "k")
  np.save(save_path, k)

  save_path = os.path.join(path, "p")
  np.save(save_path, p)


def print_array(arr):
  return str(arr).replace("\n", "")


def main(path):
  n = get_N(k)
  p = n - k # Количество проверок

  message = generate_message(k)
  print(f"Сгенерированное сообщение: {print_array(message)}")

  hamming = np.array(hamming_code(k,p,message))
  print(f"Код Хэмминга:              {print_array(hamming)}")

  hamming = make_mistake(hamming)
  print(f"Код Хэмминга с ошибкой:    {print_array(hamming)}")

  transmit(path, hamming, k, p)