# Hola 3 -> HolaHolaHola
# Angel 4 -> AngelAngelAngelAngel
# Platzi 2 -> PlatziPlatzi

import string


def make_repeater_of(n):
  def repeater(string):
    assert type(string) == str, 'Solo puedes usar strings' # ? assert condition, if False return 'Error message'
    return string * n
  return repeater


def make_division_by(n):
  def divided(number):
    assert type(number) == int, 'Solo puedes ingresar numeros' # ? assert condition, if False return 'Error message'
    return number // n # el // significa division entera.
  return divided


def run():
  repeat_5 = make_repeater_of(5)
  print(repeat_5('hola '))

  repeat_10 = make_repeater_of(10)
  print(repeat_10('Platzi '))


  division_by_3 = make_division_by(3)
  print(division_by_3(18)) # 6

  division_by_6 = make_division_by(6)
  print(division_by_6(48)) # 8


if __name__ == "__main__":
  run()