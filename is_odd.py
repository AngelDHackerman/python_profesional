

from ast import Num
from readline import read_init_file


def is_odd(numero: int) -> bool:
  contador = 0

  for i in range(1, numero + 1):
    if i == 1 or i == numero:
      continue
    if numero % i == 0:
      contador += 1
  if contador == 0:
    return True
  else: 
    return False


def run():
  if is_odd(19):
    print('Es primo')
  else:
    print('NO es primo')


if __name__ == "__main__":
  run()