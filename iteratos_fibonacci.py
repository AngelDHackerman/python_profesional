import time

class FiboIter():

  def __iter__(self):
    self.n1 = 0
    self.n2 = 1
    self.counter = 0
    return self

  def __next__(self):
    if self.counter == 0:
      self.counter += 1
      return self.n1  # creado el valor de n1. Esto es lo primero que regresara el ciclo for de abajo
    elif self.counter == 1:
      self.counter += 1
      return self.n2  # creado el valor de n2. Esto es lo segundo que retornara el ciclo for de abajo
    else:
      self.aux = self.n1 + self.n2
      # self.n1 = self.n2  # * se mueve el valor de n2 a n1
      # self.n2 = self.aux  # * n2 toma el valor actual de aux
      self.n1, self.n2 = self.n2, self.aux  # ? Swapping, hacemos lo mismo que las 2 lineas de arriba pero resumido. 
      self.counter += 1
      return self.aux  # Esto es lo que nos imprimira el ciclo for de abajo.


if __name__ == "__main__":
  fibonacci = FiboIter()  # ? Asi creamos una instancia de FiboIter
  for element in fibonacci:
    print(element)
    time.sleep(0.3)  # ? Hace esperar X seg para hacer el siguiente ciclo y poder ver como funciona la sucecion
    if element >= 100000:
      break

