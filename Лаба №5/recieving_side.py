import numpy as np
import os


def hamming_code_plus(hamming):
  s = np.sum(hamming)
  return s%2


def hamming_code_syndrom(k, p, hamming):
  S = []
  for i in range(p):
    s = 0
    l = i+1
    
    for j in range(k+p):
      bin_ = format(j+1, "b")
      bin_j = list(bin_)
      try:
        if bin_j[len(bin_j) - l]  == "1" and len(bin_j) - l >= 0:
          s += hamming[j]
      except:
        continue
    S.append(s % 2)
  S.append(hamming_code_plus(hamming))
  S2 = "".join(map(str,S))
  S2 = int(S2,2)
  if S2 == 0:
    return "Нет ошибок"
  if S[-1] == 0:
    return "Обнаружены две ошибки"

  S.pop()
  S.reverse()
  
  S = "".join(map(str, S))
  print(S)
  S = int(S, 2)
  return "Обнаружена одна ошибка под номером " + str(S)


def receive(path):
  load_path_hamming = os.path.join(path, "hamming.npy")
  load_path_k = os.path.join(path, "k.npy")
  load_path_p = os.path.join(path, "p.npy")

  hamming = np.load(load_path_hamming)
  k = np.load(load_path_k)
  p = np.load(load_path_p)
  return hamming, k, p


def print_array(arr):
  return str(arr).replace("\n", "")


def main(path):
  hamming, k, p = receive(path)
  print(f"Полученный код Хэмминга:   {print_array(hamming)}")
  h_syndrom = hamming_code_syndrom(k, p, hamming)
  print(h_syndrom)