

def run ():
  def decorador(func):
    def envoltura():    # ? este es el wrapper, donde se le agregan las demas cosas a la funcion pasada como parametro.
      print('Esto es lo que se le añade a mi funcion original')
      func()
    return envoltura

  def saludo():
    print('Hola!')

  saludo() # Hola

  saludo = decorador(saludo)  # ? Aqui se ejecuta el decorador
  saludo()
  # Esto es lo que se le añade a mi funcion original
  # Hola 


if __name__ == "__main__":
  run()


  # * esto es el azucar sintactico de los decoradores
  # @decorador
  # def saludo():
  # print('Hola!')