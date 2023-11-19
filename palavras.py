#atribuir arquivo a uma variavel
palavras_txt = "palavras.txt"

palavras = []

# with open pra liberar o arquivo assim que o bloco terminar.
with open(palavras_txt, 'r') as arquivo:
    #ler todas as linhas e adiionar a lista
    for linha in arquivo:
        palavras.append(linha.strip())  #deixando bonitinha tirando os espacos em branco
              
        
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]