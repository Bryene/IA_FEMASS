"""
feito para apos determinado valor de elementos são impostas funções
versao python: 3.11.4
"""
def get_float_list():
    # Função que solicita ao usuário a entrada de uma lista de números float e retorna a lista preenchida.
    n = int(input("Digite o número de elementos da lista: ")) # Solicita o número de elementos na lista.
    lst = [] # Inicializa uma lista vazia para armazenar os números float.
    for i in range(n):
        '''
      range gera uma sequencia númerica
      ao ser digitado esse numero, serão gerados elementos e arquivados.
      lst = lista que armazenará de forma ordenada
        '''
        num = float(input(f"Digite o {i+1}º número: ")) # Solicita e converte cada número float.
        lst.append(num) # Adiciona o número à lista.
    return lst # Retorna a lista preenchida.

def print_formatted(lst):
    # Função que recebe uma lista e imprime os valores de acordo com as especificações do enunciado.
    print(f"Valores digitados: {lst}") # Imprime a lista original.
    print(f"Valores originais em índices pares: {lst[::2]}") # Imprime os valores nos índices pares.
    print(f"Valores originais em índices ímpares: {lst[1::2]}") # Imprime os valores nos índices ímpares.
    print(f"Cada valor da lista arredondado para 1 casa decimal: {[round(num, 1) for num in lst]}") # Imprime os valores arredondados para 1 casa decimal.
    print(f"Somatório de valores contidos na lista original arredondado para 2 casas decimais: {round(sum(lst), 2)}") # Imprime a soma dos valores arredondada para 2 casas decimais.
    print(f"Cada valor da lista arredondado para inteiro: {[int(num) for num in lst]}") # Imprime os valores convertidos para inteiros.
    print(f"Do inteiro de cada valor, mostrar no sistema binário: {[bin(int(num)) for num in lst]}") # Imprime a representação binária dos inteiros.
    print(f"Do inteiro de cada valor, mostrar no sistema octal: {[oct(int(num)) for num in lst]}") # Imprime a representação octal dos inteiros.
    print(f"Do inteiro de cada valor, mostrar no sistema hexadecimal: {[hex(int(num)) for num in lst]}") # Imprime a representação hexadecimal dos inteiros.

if __name__ == '__main__':
    lst = get_float_list() # Chama a função para obter a lista de números float.
    print_formatted(lst) # Chama a função para imprimir os valores formatados.
