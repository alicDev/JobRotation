def invertString(str):
  if str == "":
    return str
  else:
    return invertString(str[1:]) + str[0]
  
print(invertString("aprovado!"))