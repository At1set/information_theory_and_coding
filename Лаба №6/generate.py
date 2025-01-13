import random


def generate_information_combination(K):
  return [random.randint(0, 1) for _ in range(K)]


def generate_cyclic_code(info_bits, generator_poly):
  n = len(info_bits) + len(generator_poly) - 1
  data = info_bits + [0] * (len(generator_poly) - 1)

  for i in range(len(info_bits)):
    if data[i] == 1:
      for j in range(len(generator_poly)):
        data[i + j] ^= generator_poly[j]

  parity_bits = data[len(info_bits):]
  return info_bits + parity_bits


def calculate_minimum_parity_bits(K):
  r = K + 1
  while r >= (2 ** (r - K) - 1):
    r += 1
  print("p:", r - K, "\n")
  return r - K


def generate_generator_poly(K):
  r = calculate_minimum_parity_bits(K)
  match r: 
    case 1:
      return [1, 1] # x + 1
    case 2:
      return [1, 1, 1] # x^2 + x + 1
    case 3:
      return [1, 0, 1, 1]  # x^3 + x + 1
    case 4:
      return [1, 1, 0, 0, 1]  # x^4 + x^3 + 1
    case 5:
      return [1, 0, 0, 0, 0, 1, 1]  # x^6 + x + 1
    case 6:
      return [1, 1, 0, 0, 0, 0, 1]  # x^6 + x^5 + 1
    case 7:
      return [1, 0, 0, 1, 1, 1, 0, 1]  # x^7 + x^4 +x^3 + x^2 + 1
    case 8:
      return [1, 0, 0, 1, 0, 1, 1, 0, 1]  # x^8 + x^5 +x^3 + x^2 + 1
    case 9:
      return [1, 0, 0, 0, 0, 1, 0, 1, 1, 1]  # x^9 + x^4 +x^2 + x + 1
    case 10:
      return [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]  # x^10 + x^3 + 1
    case _:
      return None


def get_cyclic_code(code_length):
  """
  Генерирует циклический код и образующий полином для этого кода.
  """
  start_code = generate_information_combination(code_length)
  generator_poly = generate_generator_poly(code_length)
  cyclic_code = generate_cyclic_code(start_code, generator_poly)

  return start_code, cyclic_code, generator_poly
