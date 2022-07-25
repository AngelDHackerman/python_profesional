from itertools import count
import time

def fibo_gen():
  n1 = 0 
  n2 = 1
  counter = 0
  while True:  # * se crea un ciclo infinito con el while True
    if counter == 0:
      counter += 1
      yield n1  # ? yield es igual a return, pero este no rompe la funcion, solo la pausa. Cuando se vuelva a llamar la funcion, comenzara despues de donde se pauso el ultimo yield.
    elif counter == 1:
      counter += 1
      yield n2  # Este sera el segundo valor que imprimira el ciclo de abajo
    else:
      aux = n1 + n2
      n1, n2 = n2, aux  # ? aqui se hace el swapping de python
      counter += 1
      yield aux  # Este sera uno de los valores que imprimira el ciclo de abajo


if  __name__ == "__main__":
  max_number = int(input('Cual sera el numero maximo? '))
  
  fibonacci = fibo_gen()  # debemos instanciar aun cuando es una funcion y no una clase
  for element in fibonacci:  # todo: los iterables de fibonacci son los 3 yields que estan dentro de la funcion 
    print(element)
    time.sleep(0.3)
    if element >= max_number:
      raise StopIteration