""" CODIGO INICIAL

N = int(input())

while(N > 0):
    A = str(input())
    B = str(input())
    last_numbers = A[-len(B):]
    if last_numbers == B:
        print("encaixa")
    else:
        print("nao encaixa")
    N -= 1""" 

def encaixa(A, B):
    if len(A) < len(B):
        return "nao encaixa"

    if A[-len(B):] == B:
        return "encaixa"
    else:
        return "nao encaixa"

# Entrada do usuário
N = int(input())

# Processamento dos casos de teste
casos_teste = [input().split() for _ in range(N)]
resultados = [encaixa(A, B) for A, B in casos_teste]

# Impressão dos resultados
for resultado in resultados:
    print(resultado)