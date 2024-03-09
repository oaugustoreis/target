def fibonacci(n):
  a, b = 0, 1
  sequencia = [a, b]
  for i in range(n - 2):
    a, b = b, a + b
    sequencia.append(b)
  return sequencia

def main():
  numero = 3 #definir numero 
  sequencia = fibonacci(numero + 1)
  if numero in sequencia:
    print(f"{numero} pertence à sequência de Fibonacci.")
  else:
    print(f"{numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
  main()
