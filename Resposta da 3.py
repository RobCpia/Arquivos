Fibonacci = [0, 1, 1]

while Fibonacci[-1] < 5000:
  n1 = Fibonacci[-1]
  n2 = Fibonacci[-2]
  n3 = n1 + n2
  Fibonacci.append(n3)
  print(n3)
  if Fibonacci[-1] == n1 + n2:
    print('O valor pertence a sequência de Fibonacci.\n')
  else:
    print('O valor não pertence a sequência de Fibonacci.\n')
else:
  print('Fim do Codigo.')