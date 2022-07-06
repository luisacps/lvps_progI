#LVP REPETIÇÃO 1 USANDO FOR
def main():
    n = int(input())
    for i in range(1, n + 1):
        print(i)
    return 0

if __name__ == "__main__":
    main()
    
#LVP REPETIÇÃO 1 USANDO WHILE VER.1
def main():
  n = int(input())
  x = 1
  while (x<=n):
    print(x)
    x += 1
  return 0

if __name__ == "__main__":
    main()
    
#LVP REPETIÇÃO 1 USANDO WHILE VER.2
def main():
  n = int(input())
  x = 1
  while (n>=x):
    print(x)
    x += 1
  return 0

if __name__ == "__main__":
    main()
#LVP REPETIÇÃO 2 USANDO WHILE
def main():
  x = 1
  n = int(input("numero: "))
  while (x<11):
    print(f'{x} x {n} = {x*n}')
    x += 1
  return 0

if __name__ == "__main__":
    main()
    
#LVP REPETIÇÃO 2 USANDO FOR
def main():
  n = int(input("numero: "))
  for i in range(1,11):
     print(f'{i} x {n} = {i*n}')
  return 0

if __name__ == "__main__":
    main()

#LVP REPETIÇÃO 3 
def main():
  x = 0 #pra ir somando os valores
  ler = input("quer digitar um numero? ")
  while (ler=="s"):
    n = int(input("numero: "))
    x += n
    ler = input("quer digitar um numero? ")
  print(x)
  return 0

if __name__ == "__main__":
    main()

#LVP REPETIÇÃO 4 COM WHILE 
def main():
  x = 0
  y = 0
  ler = input("deseja digitar? ")
  while (ler=="s"):
    n = int(input("numero: "))
    x += n 
    y += 1
    ler = input("deseja digitar? ")
  print(x/y)
  return 0

if __name__ == "__main__":
    main()
    
#LVP REPETIÇÃO 5 COM FOR
def main():
  for i in range(10):
    print(i)
  return 0

if __name__ == "__main__":
    main()
    
#LVP REPETIÇÃO 5 COM WHILE
def main():
  x = 0
  while (x<10):
    print(x)
    x += 1
  return 0

if __name__ == "__main__":
    main()
    
#LVP STRINGS 1 
def main():
  s1 = input()
  s2 = input()
  if (len(s1) == len(s2)):
    print("MESMO TAMANHO")
  else:
    print("TAMANHO DIFERENTE")
  if (s1==s2):
    print("CONTEÚDO IGUAL")
  else:
    print("CONTEÚDO DIFERENTE")
  return 0

if __name__ == "__main__":
    main()
    
#LVP STRINGS 1 - TENTATIVA COM FUNÇÃO
def f_verificar(x1,x2):
  if (len(x1) == len(x2)):
     print("MESMO TAMANHO")
  else:
    print("TAMANHO DIFERENTE")
  if (x1==x2):
    print("TAMANHO DIFERENTE")
  else:
    print("TAMANHO DIFERENTE")

def main():
  s1 = input()
  s2 = input()
  print(f_verificar(s1,s2))
  return 0

if __name__ == "__main__":
    main()

#STRINGS - CONTANDO A QUANTIDADE DE ESPAÇOS EM BRANCO
def main():
  a = 0
  x = input()
  for i in range(len(x)):
    if (x[i] == " "):
      a += 1
  print(f'quantidade espaços em branco {a}')
  return 0

if __name__ == "__main__":
    main()
    
#STRINGS - QUESTÃO PRÓXIMA A QUE CAIU NA PROVA
def f_brancos(frase):
  x = 0
  for i in range(len(frase)):
    if (frase[i] == " "):
      x += 1
  return x

def f_letra(frase, letra):
  y = 0
  for i in range(len(frase)):
    if (frase[i] == letra):
      y += 1
  return y
  
def main():
    f = input("digite uma frase: ")
    l = input("escolha uma letra: ")
    print(f'espaços em branco = {f_brancos(f)}')
    print(f'quantidade de letras {l} = {f_letra(f,l)}')
    return 0
    
if __name__ == "__main__":
  main()
  
#LVP STRING 2
def main():
  nome = input().upper()
  for i in range(len(nome)):
    a = nome[::-1]
  print(a)
  return 0 

if __name__ == "__main__":
  main()
  
#LVP STRING 2 - CONFORME A CORREÇAO DO PROFESSOR
def main():
  nome = input().upper()
  for i in range(len(nome)):
    a = nome[len(nome)::-1]
  print(a)
  return 0 

if __name__ == "__main__":
  main()
  
#LVP STRINGS 3
def main():
  p = input("digite uma palavra: ").upper()
  for i in range(len(p)):
    print(p[i])
  return 0

if __name__ == "__main__":
  main()

#LVP STRINGS 6 COM FUNÇÃO
def f_identificar(mes):
  if (mes == "01"):
    return "janeiro"
  elif (mes == "02"):
    return "fevereiro"
  elif (mes == "03"):
    return "março"
  elif (mes == "04"):
    return "abril"
  elif (mes == "05"):
    return "maio"
  elif (mes == "06"):
    return "junho"
  elif (mes == "07"):
    return "julho"
  elif (mes == "08"):
    return "agosto"
  elif (mes == "09"):
    return "setembro"
  elif (mes == "10"):
    return "outubro"
  elif (mes == "11"):
    return "novembro"
  elif (mes == "12"):
    return "dezembro"
  
def main():
  data = input("digite seu aniv.: ")
  d = data[:2]
  m = data[3:5]
  a = data[6:]
  print(f'{d} de {f_identificar(m)} de {a}')
  return 0

if __name__ == "__main__":
  main()

#LVP STRINGS 7 - COM FUNÇÃO
def f_branco(frase):
  y = 0
  for i in range(len(frase)):
    if (frase[i] == " "):
      y += 1
  return y
      
def main():
  a = 0
  e = 0
  i = 0
  o = 0
  u = 0
  x = input("digite uma frase: ")
  for y in range(len(x)):
    if (x[y].upper() == "A"):
      a += 1
    elif (x[y].upper() == "E"):
      e += 1
    elif (x[y].upper() == "I"):
      i += 1
    elif (x[y].upper() == "O"):
      o += 1
    elif (x[y].upper() == "U"):
      u += 1
  print(f'espaços em branco = {f_branco(x)}')
  print(f'A = {a}')
  print(f'E = {e}')
  print(f'I = {i}')
  print(f'O = {o}')
  print(f'U = {u}')
  return 0

if __name__ == "__main__":
  main()

#LVP REPETIÇÃO 6 COM FOR
def main():
  for i in range(0,11,2):
    print(i)
  return 0

if __name__ == "__main__":
  main()

#LVP REPETIÇÃO 7 COM FOR
def main():
  x = 10
  while (x>-1):
    print(x)
    x -= 1

if __name__ == "__main__":
  main()
  
#LVP REPETIÇÃO 8
def main():
  x = 0
  for i in range(5):
    nmr = int(input("digite um número: "))
    x += nmr
  print(x)
if __name__ == "__main__":
  main()
  
#LVP REPETIÇÃO 9
def main():
  x = 0 
  for i in range(1,6):
    nmr = int(input("digite um numero: "))
    x += nmr
  print(x/i)
if __name__ == "__main__":
  main()
  
#LVP REPETIÇÃO 10
def main():
  x = 0
  y = 0
  z = 0
  for i in range(1,6):
    nmr = int(input("digite um numero: "))
    if (nmr>0):
      x += nmr
    else:
      y += nmr
      z += 1
  print(f'{x} {y/z}')
  return 0 

if __name__ == "__main__":
  main()
  
#LVP REPETIÇÃO 11
def main():
  a = 0 #soma positivos
  b = 0  #soma negativos
  x = input("deseja digitar? ")
  while (x=="s"):
    nmr = int(input("digite um numero: "))
    if (nmr>0):
      a += nmr
    else:
      b += nmr
    x = input("deseja digitar? ")
  print(f'{a} {b}')
  return 0 

if __name__ == "__main__":
  main()

#LVP REPETIÇÃO 12
def main():
  a = 0 #soma positivos
  b = 0  #soma negativos
  c = 0
  x = input("deseja digitar? ")
  while (x=="s"):
    nmr = int(input("digite um numero: "))
    if (nmr>0):
      a += nmr
    else:
      b += nmr
      c += 1
    x = input("deseja digitar? ")
  print(f'{a} {b/c}')
  return 0 

if __name__ == "__main__":
  main()

#LVP REPETIÇÃO 13
def main():
  cont_m = 0
  soma_alt_mulheres = 0
  alt_mulheres = 0
  primeiro = True
  for i in range(5):
    sexo = input()
    alt = float(input())
    if (sexo=="f"): #media alt mulheres
      soma_alt_mulheres += alt
      alt_mulheres += 1
      media_alt_mulheres = soma_alt_mulheres/alt_mulheres
    elif (sexo=="m"): #quant de homens
      cont_m += 1
    if (primeiro):
      maior_alt = alt
      menor_alt = alt
      primeiro = False
    if (alt > maior_alt):
      maior_alt = alt
    if (alt < menor_alt):
      menor_alt = alt

  print(maior_alt)
  print(menor_alt)
  print(media_alt_mulheres)
  print(cont_m)
  return 0


#LVP REPETIÇÃO 19 - QUESTÃO PRÓXIMA A QUE FOI PEDIDA NA AV2
def main():
  s = 0
  a = 1
  for i in range(10):
    if (a%2 == 1): #ou seja, nmr impar
      s = s+a/a**2
    elif (a%2 == 0): #no caso de nmr par
      s = s-a/a**2
    a += 1
  print(s)
  return 0

if __name__ == "__main__":
  main()
