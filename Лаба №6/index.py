# Бацюра Илья, Вариант №43
import random

# Отправляющая сторона, генерирует циклический код и образующий полином для этого кода.
from generate import get_cyclic_code

# Принимающая сторона, находит однократные ошибки и возвращает исправленный код.
from check import check_cyclic_code


def introduce_error(code):
  error_position = random.randint(0, len(code) - 1)
  print(f"Место ошибки: {error_position + 1}")
  code_with_error = code[:]
  code_with_error[error_position] ^= 1
  return code_with_error, error_position


k = 19
exp_count = 10


def main():
  for exp_num in range(exp_count):
    exp_num += 1
    print("====================================================================================")
    print(f"Эксперимент №{exp_num}: \n")

    # Генерируем циклический код
    start_code, code, generator_poly = get_cyclic_code(k)
    print(f"Изначальный код:\n{''.join(map(str, start_code))} \n")
    print(f"Полученный циклический код:\n{''.join(map(str, code))} \n")

    # Генерация ошибки
    error_code, error_pos = introduce_error(code)
    _print = ""
    
    for i, c in enumerate(error_code):
      c = str(c)
      if i == error_pos:
        c = f"-{c}-"
      _print += c
       
    print(f"Код с единичной ошибкой:\n{_print} \n")

    # Передача на принимающую сторону
    checked_code = check_cyclic_code(exp_num, error_code, generator_poly)
    _print = ""
    
    for i, c in enumerate(checked_code):
      c = str(c)
      if i == error_pos:
        c = f"-{c}-"
      _print += c
    print(f"Исправленный код:\n{_print} \n")
    print("====================================================================================\n\n")


if __name__ == "__main__":
  main()