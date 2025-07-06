# Importa bibliotecas necessárias
import difflib
import pandas as pd
import os

# Define os nomes dos arquivos de entrada e saída
PLANILHA_ENTRADA = "similaridade\\CORRELACAO-INICIAL.xlsx"
PLANILHA_SAIDA = "similaridade\\CORRELACAO-RESULTADO.xlsx"

# Define o threshold de similaridade
TRESHOLD = 0.7

# Função para encontrar a correspondência mais próxima entre exames
def encontrar_correspondencia(exame, lista_parceira, threshold=TRESHOLD):
    """Encontra o exame mais parecido na lista da parceira, se a similaridade for acima do threshold."""
    exame = exame.upper()
    melhores = difflib.get_close_matches(exame, lista_parceira, n=1, cutoff=threshold)
    if melhores:
        return melhores[0]
    return None

def main():
    # Lista todas as abas (sheets) de uma planilha Excel:
    with pd.ExcelFile(PLANILHA_ENTRADA) as xls:
        abas = xls.sheet_names

    # Itera sobre cada aba da planilha
    # A primeira aba é considerada a da empresa, as demais são das parceiras
    for aba in abas:
        # Se for a aba da empresa, guarda os exames em uma lista "exames_empresa"
        if aba == abas[0]:
            df_base = pd.read_excel(PLANILHA_ENTRADA, sheet_name=aba)
            exames_empresa = df_base.iloc[:, 0].astype(str).tolist()
        # Se for uma aba de parceira, encontra correspondências com os exames da empresa
        else:
            df_base = pd.read_excel(PLANILHA_ENTRADA, sheet_name=aba)
            exames_parceira = df_base.iloc[:, 0].astype(str).tolist()
            # Cria um dicionário de correspondências
            correspondencias = {}
            for exame in exames_empresa:
                match = encontrar_correspondencia(exame, exames_parceira)
                correspondencias[exame] = match

            # Após gerar o dicionário de correspondências, salve em uma planilha Excel
            resultados = pd.DataFrame({
                "Exame Empresa": list(correspondencias.keys()),
                "Exame Parceira": list(correspondencias.values())
            })

            aba_resultado = abas[0] + ' X ' + aba  # Nome da aba de resultado
            # Garante que o arquivo de saída exista antes de abrir em modo append
            with pd.ExcelWriter(PLANILHA_SAIDA, mode='a' if os.path.exists(PLANILHA_SAIDA) else 'w') as writer:
                resultados.to_excel(writer, sheet_name=aba_resultado, index=False)

if __name__ == "__main__":
    main()


# Sim, você pode acessar outras abas (sheets) de uma mesma planilha usando o parâmetro 'sheet_name'
# Exemplo de como ler uma aba específica:
# df_outra_aba = pd.read_excel("exames_empresa.xlsx", sheet_name="NomeDaAba")

# Exemplo de como salvar diferentes DataFrames em diferentes abas (sheets) de uma mesma planilha Excel
# with pd.ExcelWriter("correspondencias_exames_multiplas_abas.xlsx") as writer:
#     resultados.to_excel(writer, sheet_name="Correspondencias", index=False)
#     # Exemplo: salvando o DataFrame original da empresa em outra aba
#     df_empresa.to_excel(writer, sheet_name="Exames_Empresa", index=False)
#     # Você pode adicionar outros DataFrames em outras abas conforme necessário