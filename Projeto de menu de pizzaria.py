print("seja bem vindo a pizzaria do Filipi Buffalo")

cardapio_precos = {
    'ps': {'p': 30.00, 'm': 45.00, 'g': 60.00},
    'pd': {'P': 34.00, 'm': 48.00, 'g': 66.00},
}  #Foi criado um dicionario,para que eu organizasse melhor

def fazer_pedido(): #funçao criada para todo o sistema 
    """Função para processar um único item do pedido com validação."""
    while True:
        sabor = input("Escolha o sabor desejado (PS/PD): ")
        if sabor in cardapio_precos:
            break
        else:
            print(f"Sabor inválido '{sabor}'. Tente novamente")

    while True:
        tamanho = input("Escolha o tamanho desejado (p/m/g): ")
        if tamanho in cardapio_precos[sabor]:
            break
        else:
            print(f"Tamanho inválido '{tamanho}'. Tente novamente")
    #blocos de codigo usando movimentos de repetiçao 
    preco = cardapio_precos[sabor][tamanho]
    sabor_extenso = "Pizza Salgada" if sabor == 'ps' else "Pizza Doce"
    print(f"Você pediu uma {sabor_extenso} no tamanho {tamanho}: R$ {preco:.2f}")
    return preco, sabor_extenso, tamanho


total_pedido = 0
itens_pedido = []

print(" Menu de opções (cardápio) ")

while True:
    preco_item, sabor_extenso, tamanho_item = fazer_pedido()
    total_pedido += preco_item
    itens_pedido.append(f"{sabor_extenso} tamanho {tamanho_item}")

    continuar = input("Deseja mais alguma coisa? (s/n): ")
    if continuar != 's':
        break

print(" Resumo do Pedido ")
print(f"Pedido com {len(itens_pedido)} itens:")
for item in itens_pedido:
    print(f"- {item}")
print(f"Total geral: R$ {total_pedido:.2f}")
print("ate logo e obrigado pela preferencia")
#saidas #foram usadas tambem f-strings em boa parte do codigo para que pudesse formartar os dados 



