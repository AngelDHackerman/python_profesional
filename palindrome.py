

def is_palindrome(string: str) -> bool:  # ? Como en typescript, string es de tipo "str" osea string, y -> bool significa que nos debe retornar un boolean
  string = string.replace(" ", "").lower()  # replace(" ", "") remplaza los espacios vacios por nada. 
  return string == string[::-1]

def run():
  print(is_palindrome('ana'))

if __name__ == "__main__":
  run()