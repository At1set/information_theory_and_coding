import os


def calculate_remainder(code, generator_poly):
  data = code[:]
  for i in range(len(code) - len(generator_poly) + 1):
    if data[i] == 1:
      for j in range(len(generator_poly)):
        data[i + j] ^= generator_poly[j]
  return data[-(len(generator_poly) - 1):]


def build_error_table(generator_poly, code_length):
  error_table = {}
  for error_position in range(code_length):
    error = [0] * code_length
    error[error_position] = 1
    remainder = calculate_remainder(error, generator_poly)
    error_table[tuple(remainder)] = error_position
  return error_table


def correct_error(received_code, generator_poly, error_table):
  remainder = calculate_remainder(received_code, generator_poly)
  error_position = error_table.get(tuple(remainder))

  if error_position is not None:
    received_code[error_position] ^= 1

  return received_code


def check_cyclic_code(experiment_num, code, poly):
  """
  Принимает циклический код и образующий полином.
  Находит и исправляет однократные ошибки в этом коде и возвращает исправленный код.
  """
  # Построить таблицу ошибок
  error_table = build_error_table(poly, len(code))

  # Сохранить таблицу ошибок
  if (not os.path.exists("Эксперименты")): os.mkdir("Эксперименты")
  table = ""
  with open(f"./Эксперименты/error{experiment_num}.txt", "w") as f:
    for item, value in error_table.items():
      t_str = ",".join(map(str, item)) + ": " + str(value) + "\n"
      f.write(t_str)
      table += t_str
    print(f"Таблица соответствия ошибки и вида остатка: \n{table}")
  
  # Исправить ошибку
  corrected_code = correct_error(code, poly, error_table)

  return corrected_code