# Бацюра Илья, Вариант №43
from transmitting_side import main as transmit_main
from recieving_side import main as recieve_main

exp_count = 10
k = 19
dmin = 3

def main():
  for i in range(exp_count):
    i += 1
    print("====================================================================================")
    print(f"Эксперимент №{i}: \n")
    transmit_main(i)
    recieve_main(i)
    print("====================================================================================\n\n")


if __name__ == "__main__":
  main()