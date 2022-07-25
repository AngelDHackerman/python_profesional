
# [1, 1, 2, 2, 3, 3, 4] -> [1, 2, 3, 4]

def remove_duplicates(some_list):
  without_duplicates = []

  for element in some_list:
    if element not in without_duplicates: # si el elemento no esta en without_duplicates, agregalo alli. 
      without_duplicates.append(element)
  return without_duplicates


def run():
  random_list = [1, 1, 2, 2, 3, 3, 4]
  print(remove_duplicates(random_list))

          # * reto de la clase en 2 lineas de codigo: 

def remover_duplicados(lista):
  return list(set(lista))


if __name__ == "__main__":
  run()
  print(remover_duplicados([1, 1, 2, 2, 3, 3, 4]))