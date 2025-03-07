import re

palavra = str("Olá Mundo!")
print(palavra)

#Binários pares
texto = str(input("Digite um texto binário para ser detectado: "))
print (texto)
padrao_pares =  r'\b[01]*0\b'
resultado = re.search(padrao_pares,texto)

if resultado:
    print("É binário par. ")
else:
    print("Não é par. ")  



#Palavras (binárias) com 00 no final
texto = str(input("Digite um texto binário para ser detectado se o final e 00: "))
print (texto)
padrao_pares_final = r'\b[01]*00\b'
resultado = re.findall(padrao_pares_final,texto)

if resultado:
    print("São palavras binarias com 00 no final")
else:
    print("Não são palavras binários com 00 no final")  

# Strings entre aspas
texto = str(input("digite um texto qualquer:  "))

padrao = r'(["\'])(?:(?=(\\?))\2.)*?\1'
resultado = re.findall(padrao, texto)
if resultado:
    print("Strings entre aspas")
else:
   print ("String!")

# telefones em SC
telefone = str(input("Digite um numero de telefone: "))
print (telefone)

padrao_telefone1 = r'^(47|48|49)\d{4,5}\d{4}$'  
padrao_telefone2 = r'^(47|48|49) \d{4,5}-\d{4}$' 
padrao_telefone3 = r'^(47|48|49) 9 \d{4}-\d{4}$'
padrao_telefone4 = r'^(47|48|49) 9 \d{8}$'
def validar_telefone(telefone):
    if re.match(padrao_telefone1, telefone):
        return "Número de telefone 1 aceito!"
    elif re.match(padrao_telefone2, telefone):
        return "Número de telefone2  aceito!"
    elif re.match(padrao_telefone3, telefone):
        return "Número de telefone 3  aceito!"
    elif re.match(padrao_telefone4, telefone):
        return "Número de telefone 4 aceito!"
    else:
        return "Número de telefone não aceito!"
    
print(f"{telefone}: {validar_telefone(telefone)}")    
        


# placas de veículos no Brasil
placa = str(input("Digite a placa do seu veículo: "))
print (placa)

padrao_anterior = r'^[A-Z]{3}-\d{4}$'  
padrao_atual = r'^[A-Z]{3}\d[A-Z]\d{2}$'

def validar_placa_de_carro(placa):
    if re.match(padrao_anterior, placa):
        return "Placa do veículo padrão brasileiro aceito."
   
    elif re.match(padrao_atual, placa):
        return "Placa do veículo padrão Mercosul aceito."
    else: 
        return "Padrão de placa não aceito"
    
print(f"{placa}: {validar_placa_de_carro(placa)}")    
        



# email .br ou .com.br
email = str(input("Digite seu e-mail: "))
print (email)

padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(br|com\.br)$'

def validar_email(email):
    if re.match(padrao_email, email):
        return "Email aceito!"
    else: 
        return "Não é email"
   
print(f"{email}: {validar_email(email)}")




# comentários de linha //
comentario = str(input("Agora escreva um comentario: "))
print (comentario)

padrao_comentario = r'^\/\/.*'

# Função para verificar se uma linha é um comentário
def e_comentario(cometario):
    if re.match(padrao_comentario, cometario):
        return "É comentario"
    else:
        return "Não é comentário"

print(f"{e_comentario(comentario)}")





# comentários de múltiplas linhas /* ... */
comentario_multiplas_linhas = str(input("Agora escreva um comentário em multiplas linhas: "))
print (comentario_multiplas_linhas)

padrao_comentario = r'\/\*[\s\S]*?\*\/'

# Função para verificar se uma linha é um comentário
def e_comentario_de_multiplas_linhas(comentario_multiplas_linhas):
    if re.match(padrao_comentario, comentario_multiplas_linhas):
        return "E comentário de multiplas linhas"
    else:
        return "Não é comentário de multiplas"

print(f"{e_comentario_de_multiplas_linhas(comentario_multiplas_linhas)}")