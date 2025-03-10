import re

def validar_binario_par(texto):
    padrao_pares =  r'\b[01]*0\b'
    return bool(re.search(padrao_pares, texto))


def validar_pinario_00_final(texto):
    padrao_00_final = r'\b[01]*00\b'
    return bool(re.findall(padrao_00_final,texto))


def validar_string_entre_aspas(texto):
    padrao_aspas =  r'(["\'])(?:(?=(\\?))\2.)*?\1'
    return bool(re.findall(padrao_aspas, texto))


def validar_telefone_sc(telefone):
    padrao_telefone = [
         r'^(47|48|49)\d{4,5}\d{4}$',  
         r'^(47|48|49) \d{4,5}-\d{4}$',
         r'^(47|48|49) 9 \d{4}-\d{4}$',
         r'^(47|48|49) 9 \d{8}$'
    ]
    return any(re.match(padrao, telefone) for padrao in padrao_telefone)

def validar_placa_veiculo(placa):
    padrao_anterior = r'^[A-Z]{3}-\d{4}$'  
    padrao_atual = r'^[A-Z]{3}\d[A-Z]\d{2}$'    
    return bool(re.match(padrao_anterior, placa)) or bool(re.match(padrao_atual, placa))


def valida_email(email):
    padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(br|com\.br)$'
    return bool(re.match(padrao_email, email))


def e_comentario(comentario):
    padrao_comentario = r'^\/\/.*'
    return bool(re.match(padrao_comentario, comentario))


def e_comentario_multiplas_linhas(comentario):
    padrao_comentario = r'\/\*[\s\S]*?\*\/'
    return bool(re.match(padrao_comentario, comentario))


def main():
     # binaários par
    texto = input ("Digite um texto binário para ser detectado: ")
    print("É binário par" if validar_binario_par(texto) else "Não é binriio par.") 

    # Palavras binárias com 00 no final
    texto = input ("Digite um texto binário para ser detectado se o final é 00 : ")
    print("São palavras binárias com 00 no final" if validar_pinario_00_final(texto) else "Não são plavras binárias com 00 no final")


    # Strings entre aspas
    texto = input ("Digite um texto qualaquer: ")
    print("São strings entre aspas" if validar_string_entre_aspas(texto) else "Não há string entre aspas!")


    # Telefones em SC
    telefone = input ("Digite um telefone para ser detectado: ")
    print("É um telefone em SC" if validar_telefone_sc(telefone) else "Não é um telefone em SC!")


    # Placas de veiculos no Brasil
    placa = input ("Digite uma placa de veiculo para ser detectada: ")
    print("É uma placa de veiculo no Brasil" if validar_placa_veiculo(placa) else "Não é uma placa de veiculo no Brasil")


    #Email .br. ou .com.br
    email = input ("Digite um e-mail para ser detectado: ")
    print("É um email .br ou .com.br" if valida_email(email) else "Não é e-mail")


    # Comentario de Linha //
    comentario = input("Agora escreva um comentário: ")
    print("É um comentário de linha" if e_comentario(comentario) else "Não é um comentario")


    # Comentário de multiplas linhas /*...*/
    comentario_multiplas_linhas = input("Agora esecreva um comentário de múltiplas linhas: ")
    print("É um comentário de multiplas linhas" if e_comentario_multiplas_linhas(comentario_multiplas_linhas) else "Não é comentário de múltiplas linhas!")

if __name__ == "__main__":
    main()
