
          # * Un set es un conjunto de elementos inmutables como: numeros, strings, tuplas y boleeans. 

from cgi import print_form


my_set = {3, 4, 5,}  # {3, 4, 5,}
print(my_set)

my_set2 = {'hola', 23.3, False, True} # {False, True, 'hola', 23.3}
print(my_set2)

my_set3 = {3, 3, 2}  # {3, 2}
print(my_set3)

# my_set4 = {[1, 2, 3], 4} # ! Esto es un error porque tiene un array que es mutable. 
# print(my_set4)

          # * Creando sets

empty_set = {}
print(type(empty_set))  # ? Esto es un diccionario

empty_set = set()
print(type(empty_set))  # ? Esto si es un set vacio.

          # * Casting con sets

my_list = [1, 1, 2, 2, 3, 3, 4, 4, 5]
my_set = set(my_list)
print(my_set)  # {1, 2, 3, 4, 5}

my_tuple = ('hola', 'hola', 'hola', 1)
my_set2 = set(my_tuple)
print(my_set2)  # {'hola', 1} 

          # * Añadir elementos a un set

my_set = {1, 2, 3}
print(my_set)  # {1, 2, 3}

# Añadir un elemento

my_set.add(4)
print(my_set)  # {1, 2, 3}

# Añadir multiples elementos

my_set.update([1, 2, 5])
print(my_set)  # {1, 2, 3, 4, 5}

# Añadir multiples elementos

my_set.update((1, 7, 2), {6, 8})
print(my_set)  # {1, 2, 3, 4, 5, 6, 7, 8}

          # * Borrar elementos de un set

my_set = {1, 2, 3, 4, 5, 6, 7}
print(my_set)  # {1, 2, 3, 4, 5, 6, 7}

# Borrar un elemento existente

my_set.discard(1)
print(my_set)  # {2, 3, 4, 5, 6, 7}

# Borrar un elemento existente 

my_set.remove(2)
print(my_set)  # {3, 4, 5, 6, 7}

# Borrar un elemento inexistente

my_set.discard(10)  # ? Con discard NO hay problema si "eliminamos" elementos inexistentes
print(my_set)  # {3, 4, 5, 6, 7}

# Borrar un elemento inexistente

# my_set.remove(12) 
# print(my_set)  # ! error, remove no puede 'eliminar' elementos inexistentes

my_set = {1, 2, 3, 4, 5, 6, 7}

# Borrar un elemento aleatorio

my_set.pop() # ? Con esto borramos un elemento aleatorio
print(my_set)

# Limpiar el set

my_set.clear()  # ? Se eliminan todos los datos del set o conjunto. 
print(my_set)
