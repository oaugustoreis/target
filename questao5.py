def inverter_string(texto):
 
  texto_invertido = ""
  for i in range(len(texto)-1, -1, -1):
    texto_invertido += texto[i]
  return texto_invertido

texto = "Target Sistemas"
texto_invertido = inverter_string(texto)
print(texto)
print(texto_invertido)
