print("Seja bem vindo à Madeireira • Proprietário: Filipi Buffalo")

def calcular_valor_total(tipo_madeira, qtd_toras, tipo_transporte):
    """Calcula o valor final da conta de toras de madeira com base nas regras fornecidas."""
    #funçao criada para organizar tipo,quantidade,valores e transporte
    precos_madeira = {
        'PIN': 150.40,
        'PER': 170.20,
        'MOG': 190.90,
        'IPE': 210.10,
        'IMB': 220.70,
    }

    custos_transporte = {
        1: 1000.00,
        2: 2000.00,
        3: 2500.00,
    }

    if tipo_madeira not in precos_madeira:
        return "Erro: Tipo de madeira inválido."
    if tipo_transporte not in custos_transporte:
        return "Erro: Tipo de transporte inválido."
    if qtd_toras > 2000:
        return "Erro: Pedidos acima de 2000 m³ não são aceitos."

    # Descontos por quantidade
    desconto = 0
    if 100 <= qtd_toras < 500:
        desconto = 0.04
    elif 500 <= qtd_toras < 1000:
        desconto = 0.09
    elif 1000 <= qtd_toras <= 2000:
        desconto = 0.16

    preco_base_m3 = precos_madeira[tipo_madeira]
    custo_transporte = custos_transporte[tipo_transporte]

    valor_bruto = preco_base_m3 * qtd_toras
    valor_com_desconto = valor_bruto * (1 - desconto)

    valor_total = valor_com_desconto + custo_transporte

    return round(valor_total, 2)


 #    MENU PRINCIPAL


while True:
    print("\n===== MENU DE MADEIRAS =====")      #bloco de continuaçao
    print("PIN - Pinho  (R$ 150,40 por m³)")
    print("PER - Peroba (R$ 170,20 por m³)")
    print("MOG - Mogno  (R$ 190,90 por m³)")
    print("IPE - Ipê    (R$ 210,10 por m³)")
    print("IMB - Imbuia (R$ 220,70 por m³)")

    tipo = input("\nEscolha o tipo de madeira (PIN/PER/MOG/IPE/IMB): ").strip().upper()

    try:
        qtd = float(input("Informe a quantidade em m³: "))
    except ValueError:
        print("❌ Quantidade inválida!")
        continue

    print("\nTipos de transporte:")
    print("1 - Rodoviário (R$ 1000)")
    print("2 - Ferroviário (R$ 2000)")
    print("3 - Hidroviário (R$ 2500)")   #primeira saida de resultados

    try:
        transporte = int(input("Escolha o tipo de transporte (1/2/3): "))
    except ValueError:
        print("❌ Transporte inválido!")
        continue

    total = calcular_valor_total(tipo, qtd, transporte)

    print("\n===== RESULTADO DO PEDIDO =====")
    print(f"Total a pagar: {total}")             #foram usados metodos de leitura de letra maiuscula

    continuar = input("\nDeseja fazer outro pedido? (S/N): ").strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input("Digite apenas S ou N: ").strip().upper()

    if continuar == 'N':
        print("\nObrigado por comprar com a Madeireira Buffalo! Volte sempre! 🌲")
        break     #fim do codigo com uma mensagem 