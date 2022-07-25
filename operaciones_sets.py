
          # * Union de sets

my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 | my_set2
print(my_set3)  # {3, 4, 5, 6, 7}

          # * Elementos en comun

my_set4 = my_set1 & my_set2
print(my_set4)  # {5}

          # * Diferencia, me quedo con los elementos que no se comparten con el otro set

my_set5 = my_set1 - my_set2
print(my_set5)  # {3, 4}

my_set6 = my_set2 - my_set1
print(my_set6)  # {6, 7}

          # * Diferencia simetrica, une ambos elementos pero elimina los elementos compartidos

my_set7 = my_set1 ^ my_set2
print(my_set7)  # {3, 4, 6, 7}

