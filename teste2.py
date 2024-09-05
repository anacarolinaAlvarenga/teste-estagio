print('Resposta da questão 2.')

def pertence_fibonacci(num):
  """Verifica se um número pertence à sequência de Fibonacci.

  Args:
    num: O número a ser verificado.

  Returns:
    True se o número pertence à sequência, False caso contrário.
  """

  a, b = 0, 1
  while b <= num:
    if b == num:
      return True
    a, b = b, a + b
  return False

# Solicita o número ao usuário
numero = int(input("Digite um número: "))

# Verifica se o número pertence à sequência de Fibonacci
if pertence_fibonacci(numero):
  print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
  print(f"O número {numero} não pertence à sequência de Fibonacci.")