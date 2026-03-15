# ==========================================
# 0. BIBLIOTECAS
# ==========================================
import csv # Utilizada para baixar o arquivo .csv com todos os registros feitos pelo usuário
import os  # Utilizada para guardar o arquivo .csv gerado no mesmo diretório deste código Python

# ==========================================
# 1. ÁREA DAS FUNÇÕES
# ==========================================

def calculo_produtividade(yn):
            produtividade = ["Alta", "Média", "Baixa"]
            produtividade_valores = [60, 35, 20]

            produtividade_yn = input(f"Você sabe informar a sua produtividade média {yn}? ").lower().strip()
            # Loop que força o usuário a selecionar uma opção válida
            while produtividade_yn not in yn:
                produtividade_yn = input("Opção inválida. Por favor digite 'sim' ou 'não': ")

            if produtividade_yn == "sim":
                produtividade_media = float(input("Digite a produtividade média de sua safra em sacas por hectare: "))

            else:
                print("A produtividade do café pode variar bastante dependendo da região, manejo e clima. Como referência aproximada, considere:\n"
                    f"1. {produtividade[0]} - cerca de 60 sacas/ha ou mais.\n"
                    f"2. {produtividade[1]} - cerca de 35 sacas/ha.\n"
                    f"3. {produtividade[2]} - cerca de 20 sacas/ha."
                )
                produtividade_media = int(input("Digite 1, 2 ou 3: "))

                # Loop que força o usuário a selecionar uma opção válida
                while produtividade_media not in [1, 2, 3]:
                    produtividade_media = int(input(f"Opção inválida. Por favor digite um valor válido [1. {produtividade[0]}, 2. {produtividade[1]}, 3. {produtividade[2]}]: "))
                
                produtividade_indice = produtividade_media - 1
                produtividade_media = produtividade_valores[produtividade_indice]
                print(f"Considerando uma produtividade {produtividade[produtividade_indice].lower()} de {produtividade_valores[produtividade_indice]} sacas por hectare.")

            return produtividade_media

def calculo_espacamento(yn):  
            espacamento_yn = input(f"Você sabe informar o espaçamento entre linhas e plantas que pretende utilizar {yn}? ").lower().strip()

            while espacamento_yn not in yn:
                espacamento_yn = input("Opção inválida. Por favor digite 'sim' ou 'não': ")

            if espacamento_yn == "sim":
                # Espaçamento entre linhas
                while True:
                    espacamento_linhas = float(input("Digite o espaçamento entre linhas em metros: "))

                    if 3 <= espacamento_linhas <= 4:
                        print(f"Considerando um espaçamento entre linhas de {espacamento_linhas} metros.")
                        break

                    print(f"O espaçamento de linha de {espacamento_linhas} metro(s) não é o mais adequado para o plantio de café.")

                    espacamento_yn = input(f"Mesmo assim, deseja prosseguir com esse valor {yn}? ").lower().strip()

                    while espacamento_yn not in yn:
                        espacamento_yn = input("Opção inválida. Por favor digite 'sim' ou 'não': ")

                    if espacamento_yn == "sim":
                        print(f"Considerando um espaçamento entre linhas de {espacamento_linhas} metros.")
                        break


                # Espaçamento entre plantas
                while True:
                    espacamento_plantas = float(input("Digite o espaçamento entre plantas em metros: "))

                    if 0.5 <= espacamento_plantas <= 1.0:
                        print(f"Considerando um espaçamento entre plantas de {espacamento_plantas} metros.")
                        break

                    print(f"O espaçamento entre plantas de {espacamento_plantas} metros pode não ser ideal para o plantio de café.")

                    espacamento_yn = input(f"Mesmo assim, deseja prosseguir com esse valor {yn}? ").lower().strip()

                    while espacamento_yn not in yn:
                        espacamento_yn = input("Opção inválida. Por favor digite 'sim' ou 'não': ")

                    if espacamento_yn == "sim":
                        print(f"Prosseguindo com um espaçamento entre plantas de {espacamento_plantas} metros.")
                        break

            else:
                print("Caso não saiba os espaçamentos ideais, podemos utilizar valores médios recomendados para o cultivo de café.")

                espacamento_linhas_sugestao = 3.5
                espacamento_plantas_sugestao = 0.75

                print(
                    f"Sugestão:\n"
                    f"Espaçamento entre linhas: {espacamento_linhas_sugestao} metros\n"
                    f"Espaçamento entre plantas: {espacamento_plantas_sugestao} metros"
                )

                espacamento_yn = input(f"Deseja utilizar esses valores sugeridos {yn}? ").lower().strip()

                while espacamento_yn not in yn:
                    espacamento_yn = input("Opção inválida. Por favor digite 'sim' ou 'não': ")

                if espacamento_yn == "sim":
                    espacamento_linhas = espacamento_linhas_sugestao
                    espacamento_plantas = espacamento_plantas_sugestao
                    print(
                        f"Considerando espaçamento de {espacamento_linhas} metros entre linhas "
                        f"e {espacamento_plantas} metros entre plantas."
                    )

                else:
                    # Espaçamento entre linhas
                    while True:
                        espacamento_linhas = float(input("Digite o espaçamento entre linhas em metros: "))

                        if 3 <= espacamento_linhas <= 4:
                            print(f"Considerando um espaçamento entre linhas de {espacamento_linhas} metros.")
                            break

                        print(f"O espaçamento de linha de {espacamento_linhas} metro(s) não é o mais adequado para o plantio de café.")

                        espacamento_yn = input(f"Mesmo assim, deseja seguir com esse valor {yn}? ").lower().strip()

                        while espacamento_yn not in yn:
                            espacamento_yn = input("Opção inválida. Por favor digite 'sim' ou 'não': ")

                        if espacamento_yn == "sim":
                            print(f"Considerando um espaçamento entre linhas de {espacamento_linhas} metros.")
                            break


                    # Espaçamento entre plantas
                    while True:
                        espacamento_plantas = float(input("Digite o espaçamento entre plantas em metros: "))

                        if 0.5 <= espacamento_plantas <= 1.0:
                            print(f"Considerando um espaçamento entre plantas de {espacamento_plantas} metros.")
                            break

                        print(f"O espaçamento entre plantas de {espacamento_plantas} metros pode não ser ideal para o plantio de café.")

                        espacamento_yn = input(f"Mesmo assim, deseja seguir com esse valor {yn}? ").lower().strip()

                        while espacamento_yn not in yn:
                            espacamento_yn = input("Opção inválida. Por favor digite 'sim' ou 'não': ")

                        if espacamento_yn == "sim":
                            print(f"Prosseguindo com um espaçamento entre plantas de {espacamento_plantas} metros.")
                            break

            return espacamento_linhas, espacamento_plantas

def calculo_talhao(area, plantas_ha):
    
    print("\nComo deseja dividir os talhões?")
    print("1 - Talhões iguais")
    print("2 - Talhões com tamanhos diferentes")

    opcao = int(input("Escolha uma opção: "))

    while opcao not in [1, 2]:
        opcao = int(input("Opção inválida. Por favor digite 1 ou 2: "))

    talhoes = []

    if opcao == 1:
        talhao = int(input("Em quantos talhões deseja dividir a área: "))
        area_talhao = area / talhao

        for i in range(talhao):
            plantas = area_talhao * plantas_ha
            lado = (area_talhao * 10000) ** 0.5

            talhoes.append({
                "area": area_talhao,
                "plantas": plantas,
                "lado_a": lado,
                "lado_b": lado
            })

    else:
        talhao = int(input("Quantos talhões deseja criar: "))
        soma = 0

        for i in range(talhao):
            if i < talhao - 1:
                # TRAVA DE SEGURANÇA ADICIONADA AQUI
                while True:
                    area_talhao = float(input(f"Área do talhão {i+1} (ha): "))
                    
                    if area_talhao <= 0:
                        print("❌ A área do talhão precisa ser maior que zero.")
                    elif (soma + area_talhao) >= area:
                        area_disponivel = area - soma
                        print(f"❌ Valor inválido! Você precisa deixar espaço para os próximos talhões.")
                        print(f"A área máxima que você pode usar agora sem zerar o último talhão é menor que {area_disponivel:.2f} ha.")
                    else:
                        soma += area_talhao
                        break # Se o valor for válido, sai do laço e continua
            else:
                # último talhão precisa fechar a área total
                restante = area - soma
                area_talhao = float(input(f"Área do último talhão (ha). Para fechar a área total de {area} ha, o valor deve ser {restante:.2f}: "))

                while abs((soma + area_talhao) - area) > 0.001:
                    print("A soma das áreas não bate com a área total informada.")
                    area_talhao = float(input(f"Digite novamente a área do último talhão (valor esperado igual a {restante:.2f} ha): "))

                soma += area_talhao

            plantas = area_talhao * plantas_ha
            lado = (area_talhao * 10000) ** 0.5

            talhoes.append({
                "area": area_talhao,
                "plantas": plantas,
                "lado_a": lado,
                "lado_b": lado
            })

    print("\n" + "-"*40)
    print("📐 Nota: Para fins de cálculo das dimensões externas, estamos considerando que os talhões possuem o formato geométrico de um QUADRADO perfeito.")
    print("-"*40)

    print("\nResumo dos Talhões:")
    for i, t in enumerate(talhoes):
        print(f"\nTalhão {i+1}")
        print(f"Área: {t['area']:.2f} ha")
        print(f"Plantas: {t['plantas']:.0f}")
        print(f"Lado A: {t['lado_a']:.2f} m")
        print(f"Lado B: {t['lado_b']:.2f} m")

    return talhoes

def calculo_insumos(cultura, area_total, espacamento_linhas):
    # Calculando os metros lineares (as "ruas") para cumprir a Regra C
    metros_lineares_ha = 10000 / espacamento_linhas
    metros_totais = metros_lineares_ha * area_total

    tabela_base = {
        "café": [
            {"nome": "Fósforo (P2O5)", "dose_media": 140, "unidade": "kg"},
            {"nome": "Nitrogênio (N)", "dose_media": 300, "unidade": "kg"},
            {"nome": "Potássio (K2O)", "dose_media": 225, "unidade": "kg"},
            {"nome": "Fungicidas/Inseticidas", "dose_media": 0.75, "unidade": "L"},
            {"nome": "Calda de pulverização", "dose_media": 300, "unidade": "L"}
        ],
        "soja": [
            {"nome": "Fósforo (P2O5)", "dose_media": 90, "unidade": "kg"},
            {"nome": "Potássio (K2O)", "dose_media": 100, "unidade": "kg"},
            {"nome": "Inoculante", "dose_media": 0.15, "unidade": "L"}, 
            {"nome": "Herbicidas", "dose_media": 3, "unidade": "L"},
            {"nome": "Fungicidas", "dose_media": 0.45, "unidade": "L"},
            {"nome": "Calda de pulverização", "dose_media": 150, "unidade": "L"}
        ]
    }

    print(f"\n🚜 Relatório de Insumos Recomendados para {area_total} ha de {cultura.capitalize()}:")
    print(f"📏 A lavoura possui aproximadamente {metros_totais:.0f} metros lineares de ruas.")
    
    insumos_calculados = {}
    for insumo in tabela_base[cultura]:
        # 1. Descobre a dosagem exata por metro linear da rua
        dose_por_metro = insumo["dose_media"] / metros_lineares_ha
        
        # 2. Calcula a quantidade total usando os metros totais (Atendendo ao item C do projeto)
        quantidade_total = dose_por_metro * metros_totais    
        
        insumos_calculados[insumo["nome"]] = quantidade_total
        
        # O print agora mostra a quantidade total e também quanto está sendo gasto por metro!
        print(f" - {insumo['nome']}: {quantidade_total:.2f} {insumo['unidade']} (Aprox. {dose_por_metro:.4f} {insumo['unidade']}/metro)")
        
    return insumos_calculados

# ==========================================
# 2. FUNÇÃO PRINCIPAL E MENU
# ==========================================
def main(): 
    # Vator que guarda todos os talhões e culturas cadastradas.
    banco_de_dados = []
    yn = ["sim", "não"]

    # Loop infinito para manter o menu rodando até o usuário escolher "Sair"
    while True:
        print("\n" + "="*35)
        print("🌾 SISTEMA FARM TECH SOLUTIONS 🌾")
        print("="*35)
        print("1. Cadastrar área/cultura (Entrada)")
        print("2. Visualizar cadastros (Saída)")
        print("3. Atualizar um cadastro")
        print("4. Deletar um cadastro")
        print("5. Exportar dados para Estatística (Gerar CSV)")
        print("6. Sair do programa")
        print("="*35)

        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == '1':
            print("\n>> Você escolheu: Cadastrar área/cultura.")
            
            while True:
                cultura_escolhida = input("Qual cultura deseja cadastrar (café/soja)? ").lower().strip()
                if cultura_escolhida in ['café', 'soja']:
                    break 
                else:
                    print("\n❌ Cultura não reconhecida. Tente novamente.")
            
            if cultura_escolhida == 'café':
                print("\n--- Iniciando cálculos para o Café ---")
                area = float(input("Digite a área disponível para plantio em hectares: "))
                
                produtividade_media = calculo_produtividade(yn)
                espacamento_linhas, espacamento_plantas = calculo_espacamento(yn)
                
                # Cálculo Plantas por Hectare - Café
                plantas_ha = 10000 / (espacamento_linhas * espacamento_plantas)
                print(f"Com esse espaçamento cabem aproximadamente {plantas_ha:.0f} plantas por hectare.")
                
                # Chama a divisão de talhões
                talhoes = calculo_talhao(area, plantas_ha)
                relatorio_insumos = calculo_insumos('café', area, espacamento_linhas)
                
                cadastro = {
                    "id": len(banco_de_dados) + 1,
                    "cultura": "café",
                    "area_total": area,
                    "produtividade": produtividade_media,
                    "talhoes": talhoes,
                    "insumos": relatorio_insumos
                }
                banco_de_dados.append(cadastro)
                print(f"\n✅ Cadastro do Café (ID {cadastro['id']}) salvo com sucesso!")

            elif cultura_escolhida == 'soja':
                print("\n--- Iniciando cálculos para a Soja ---")
                area = float(input("Digite a área disponível para plantio em hectares: "))
                produtividade_media = float(input("Digite a produtividade média esperada (ex: 60 sacas/ha): "))
                
                # Cálculo de sementes por metro - Soja
                espacamento_linhas_soja = 0.45
                sementes_por_metro = 14
                plantas_ha = (10000 / espacamento_linhas_soja) * sementes_por_metro
                print(f"No padrão da soja, cabem aproximadamente {plantas_ha:.0f} sementes por hectare.")
                
                # Chama a divisão de talhões
                talhoes = calculo_talhao(area, plantas_ha)
                relatorio_insumos = calculo_insumos('soja', area, espacamento_linhas_soja)
                
                cadastro = {
                    "id": len(banco_de_dados) + 1,
                    "cultura": "soja",
                    "area_total": area,
                    "produtividade": produtividade_media,
                    "talhoes": talhoes,
                    "insumos": relatorio_insumos
                }
                banco_de_dados.append(cadastro)
                print(f"\n✅ Cadastro da Soja (ID {cadastro['id']}) salvo com sucesso!")
                
            input("\n[Pressione ENTER para voltar ao menu principal...]")

        elif opcao == '2':
            print("\n>> Você escolheu: Visualizar cadastros.")
            
            # 1. Verifica se o vetor está vazio
            if len(banco_de_dados) == 0:
                print("Ainda não há nenhuma área cadastrada no sistema.")
            
            else:
                print("\n" + "-"*40)
                print("📋 RELATÓRIO DE ÁREAS CADASTRADAS 📋")
                print("-"*40)
                
                for cadastro in banco_de_dados:
                    print(f"\n🏷️  ID do Cadastro: {cadastro['id']}")
                    print(f"🌱 Cultura: {cadastro['cultura'].capitalize()}")
                    print(f"📏 Área Total: {cadastro['area_total']} ha")
                    print(f"📈 Produtividade: {cadastro['produtividade']} sacas/ha")
                    
                    # Esse loop for serve para listar todos os talhões cadastrados
                    print("   Detalhes da Divisão:")
                    for i, talhao in enumerate(cadastro['talhoes']):
                        print(f"     - Talhão {i+1}: {talhao['area']:.2f} ha | {talhao['plantas']:.0f} plantas cadastradas")

                    print("   Insumos Necessários:")
                    for nome_insumo, qtde in cadastro['insumos'].items():
                        print(f"     - {nome_insumo}: {qtde:.2f}")
                        
                    print("-" * 40)
            
            input("\n[Pressione ENTER para voltar ao menu principal...]") 

        elif opcao == '3':
            print("\n>> Você escolheu: Atualizar um cadastro.")
            
            if len(banco_de_dados) == 0:
                print("Ainda não há nenhuma área cadastrada para atualizar.")
            else:
                print("\n📋 IDs disponíveis no sistema:")
                for cadastro in banco_de_dados:
                    print(f"🏷️  ID: {cadastro['id']} - Cultura: {cadastro['cultura'].capitalize()}")
                
                # Loop principal de validação do ID
                while True:
                    id_str = input("\nDigite o ID do cadastro que deseja atualizar (ou '0' para cancelar): ").strip()
                    
                    if id_str == '0':
                        print("Atualização cancelada.")
                        break

                    if id_str.isdigit():
                        id_atualizar = int(id_str)
                        cadastro_encontrado = False
                        
                        # Percorre o vetor procurando o ID
                        for cadastro in banco_de_dados:
                            if cadastro['id'] == id_atualizar:
                                cadastro_encontrado = True
                                print(f"\n✅ Cadastro ID {id_atualizar} encontrado!")
                                
                                # Submenu
                                print("\nO que você deseja atualizar nesse cadastro?")
                                print("1. Apenas a Produtividade Média")
                                print("2. Refazer cálculos estruturais (Área Total, Espaçamento, Talhões e Insumos)")
                                
                                # Prende o usuário até ele escolher 1 ou 2
                                while True:
                                    escolha_alt = input("Escolha uma opção (1 ou 2): ").strip()
                                    if escolha_alt in ['1', '2']:
                                        break
                                    print("❌ Opção inválida. Digite 1 ou 2.")

                                # Executa a escolha do submenu
                                # Executa a escolha do submenu
                                if escolha_alt == '1':
                                    print(f"\nA produtividade atual é de {cadastro['produtividade']} sacas/ha.")
                                    print("Vamos atualizar esse valor:")
                                    
                                    # Separa por cultura!
                                    if cadastro['cultura'] == 'café':
                                        nova_produtividade = calculo_produtividade(yn)
                                    else:
                                        nova_produtividade = float(input("Digite a nova produtividade média esperada: "))
                                        
                                    cadastro['produtividade'] = nova_produtividade
                                    print("\n✅ Produtividade atualizada com sucesso!")

                                elif escolha_alt == '2':
                                    print("\n⚠️ Atenção: Isso irá sobrepor os dados antigos de área, talhões e insumos.")
                                    nova_area = float(input("Digite a nova área disponível para plantio em hectares: "))
                                    
                                    # Separa a matemática por cultura!
                                    if cadastro['cultura'] == 'café':
                                        novo_esp_lin, novo_esp_plan = calculo_espacamento(yn)
                                        plantas_ha = 10000 / (novo_esp_lin * novo_esp_plan)
                                    else:
                                        novo_esp_lin = 0.45
                                        plantas_ha = (10000 / novo_esp_lin) * 14
                                        print(f"Mantendo o padrão da soja ({novo_esp_lin}m entre linhas).")
                                    
                                    # As funções comuns para as duas culturas
                                    novos_talhoes = calculo_talhao(nova_area, plantas_ha)
                                    novos_insumos = calculo_insumos(cadastro['cultura'], nova_area, novo_esp_lin)

                                    # Atualiza os dados direto no vetor
                                    cadastro['area_total'] = nova_area
                                    cadastro['talhoes'] = novos_talhoes
                                    cadastro['insumos'] = novos_insumos
                                    print("\n✅ Cálculos estruturais e de insumos atualizados com sucesso!")
                        
                        if cadastro_encontrado:
                            break
                        else:
                            print(f"\n❌ O ID {id_atualizar} não foi encontrado no sistema.")
                    
                    else:
                        print("\n❌ Por favor, digite apenas números inteiros para o ID.")

            input("\n[Pressione ENTER para voltar ao menu principal...]")

        elif opcao == '4':
            print("\n>> Você escolheu: Deletar um cadastro.")
            
            if len(banco_de_dados) == 0:
                print("Ainda não há nenhuma área cadastrada para deletar.")
            else:
                print("\n📋 IDs disponíveis para exclusão:")
                for cadastro in banco_de_dados:
                    print(f"🏷️  ID: {cadastro['id']} - Cultura: {cadastro['cultura'].capitalize()}")
                
                while True:
                    id_str = input("\nDigite o ID do cadastro que deseja deletar (ou '0' para cancelar): ").strip()
                    
                    if id_str == '0':
                        print("Operação de exclusão cancelada.")
                        break

                    if id_str.isdigit():
                        id_deletar = int(id_str)
                        cadastro_encontrado = False
                        
                        # Percorre o vetor usando enumerate para saber o índice do cadastro a ser deletado
                        for indice, cadastro in enumerate(banco_de_dados):
                            if cadastro['id'] == id_deletar:
                                cadastro_encontrado = True
                                
                                # Deletando o item do vetor
                                del banco_de_dados[indice]
                                
                                print(f"\n🗑️  Sucesso! O Cadastro ID {id_deletar} foi removido do sistema.")
                                break
                        
                        if cadastro_encontrado:
                            break
                        else:
                            print(f"\n❌ O ID {id_deletar} não foi encontrado no sistema.")
                    
                    else:
                        print("\n❌ Por favor, digite apenas números inteiros para o ID.")

            input("\n[Pressione ENTER para voltar ao menu principal...]")

        elif opcao == '5':
            print("\n>> Você escolheu: Exportar dados para Estatística.")
            
            if not banco_de_dados:
                print("\n❌ Ação cancelada: Não há dados cadastrados no sistema para exportar.")
                print("Por favor, volte na opção 1 e cadastre pelo menos uma área primeiro.")
            else:
                import os
                import csv # Garantindo que o csv está importado
                
                diretorio_atual = os.path.dirname(os.path.abspath(__file__))
                nome_arquivo = os.path.join(diretorio_atual, "dados_farmtech.csv")
                
                with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
                    # 1. Definimos TODAS as colunas possíveis (O "Tudo" que você pediu)
                    colunas = [
                        'ID', 'Cultura', 'Area_Total_ha', 'Produtividade_Sacas_ha', 
                        'Producao_Total_Sacas', 'Qtd_Talhoes', 'Total_Plantas_Sementes',
                        'Media_Tamanho_Talhao_ha', # Pegando a média do tamanho dos talhões
                        # Todos os Insumos possíveis de Café e Soja:
                        'Insumo_Fosforo_kg', 'Insumo_Nitrogenio_kg', 'Insumo_Potassio_kg', 
                        'Insumo_Inoculante_L', 'Insumo_Herbicidas_L', 'Insumo_Fungicidas_L', 
                        'Insumo_Calda_Pulverizacao_L'
                    ]
                    
                    escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)
                    escritor.writeheader()
                    
                    for cadastro in banco_de_dados:
                        # Achata os dados de Talhões
                        qtd_talhoes = len(cadastro['talhoes'])
                        total_plantas = sum(t['plantas'] for t in cadastro['talhoes'])
                        media_talhao = cadastro['area_total'] / qtd_talhoes if qtd_talhoes > 0 else 0
                        
                        # Puxa os insumos com .get() (Se a cultura não usa esse insumo, preenche com 0)
                        insumos = cadastro['insumos']
                        
                        escritor.writerow({
                            'ID': cadastro['id'],
                            'Cultura': cadastro['cultura'],
                            'Area_Total_ha': cadastro['area_total'],
                            'Produtividade_Sacas_ha': cadastro['produtividade'],
                            'Producao_Total_Sacas': round(cadastro['area_total'] * cadastro['produtividade'], 2),
                            'Qtd_Talhoes': qtd_talhoes,
                            'Total_Plantas_Sementes': round(total_plantas, 0),
                            'Media_Tamanho_Talhao_ha': round(media_talhao, 2),
                            
                            # Mapeando todos os insumos calculados
                            'Insumo_Fosforo_kg': round(insumos.get('Fósforo (P2O5)', 0), 2),
                            'Insumo_Nitrogenio_kg': round(insumos.get('Nitrogênio (N)', 0), 2),
                            'Insumo_Potassio_kg': round(insumos.get('Potássio (K2O)', 0), 2),
                            'Insumo_Inoculante_L': round(insumos.get('Inoculante', 0), 2),
                            'Insumo_Herbicidas_L': round(insumos.get('Herbicidas', 0), 2),
                            # O Café usa "Fungicidas/Inseticidas" e a Soja "Fungicidas", vamos juntar os dois:
                            'Insumo_Fungicidas_L': round(insumos.get('Fungicidas', insumos.get('Fungicidas/Inseticidas', 0)), 2),
                            'Insumo_Calda_Pulverizacao_L': round(insumos.get('Calda de pulverização', 0), 2)
                        })
                        
                print(f"\n✅ Sucesso! O arquivo 'dados_farmtech.csv' foi gerado com a totalidade dos dados cadastrados!")
                print("Arquivo salvo em:", nome_arquivo)
                
            input("\n[Pressione ENTER para voltar ao menu principal...]")

        elif opcao == '6':
            print("\n>> Encerrando o sistema. Até logo!")
            break

        else:
            print("\n>> Opção inválida! Por favor, digite um número de 1 a 5.")

# ==========================================
# 3. PONTO DE PARTIDA
# ==========================================
if __name__ == "__main__":
    main()