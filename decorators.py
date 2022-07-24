from datetime import datetime

def run():
  def execution_time(func):
    def wrapper(*args, **kwargs):  # ! *args: No importa la cantidad de argumentos Posicionales que se le envien, **kwargs: NO importa la cantida de argumentos Nombrados que se le envien
      initial_time = datetime.now()
      func(*args, **kwargs)
      final_time = datetime.now()
      time_elapsed = final_time - initial_time
      print(f'Pasaron {str(time_elapsed.total_seconds())} segundos')
    return wrapper

  @execution_time
  def random_func():
    for _ in range(1, 100000):
      pass

  random_func()

  @execution_time
  def suma(a: int, b: int) -> int:
    return a + b

  suma(5, 6)



if __name__ == "__main__":
  run()