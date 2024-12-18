# Бацюра Илья, Вариант №43
import os
from transmitting_side import main as transmit_main
from recieving_side import main as recieve_main

exp_count = 10
k = 50
folder_path = fr"D:\At1set\Учеба\Теория информации и кодирование\Лаба №5\Эксперименты"

def main():
  for i in range(exp_count):
    i += 1
    path = os.path.join(folder_path, f"Эксперимент №{i}")
    print("====================================================================================")
    print(f"Эксперимент №{i}: \n")
    transmit_main(path)
    recieve_main(path)
    print("====================================================================================\n\n")


if __name__ == "__main__":
  main()