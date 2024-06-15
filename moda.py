# Bibliotecas
import statistics as st

# Dados salariais
dados = {
    "Empresa Itau": [1000, 6000, 1200, 8000, 1400],
    "Empresa Google": [5000, 4000, 3000, 2000, 7000],
    "Empresa C6": [1200, 1300, 8000, 3000, 15000],
    "Empresa Aws": [1400, 1750, 2000, 4500, 5900, 7000],
}


def mediaSalario(dados):
  return sum(dados) / len(dados)

def modaSalario(dados):
  contagem_valores = []
  for valor in dados:
    contagem_valores.append(dados.count(valor))
  return dados[contagem_valores.index(max(contagem_valores))]

def medianaSalario(dados):
  dados_ordenados = sorted(dados)
  tamanho_lista = len(dados_ordenados)
  meio_lista = tamanho_lista // 2
  if tamanho_lista % 2 == 0:
    return (dados_ordenados[meio_lista - 1] + dados_ordenados[meio_lista]) / 2
  else:
    return dados_ordenados[meio_lista]

def desvio(dados):
  media_valores = medianaSalario(dados)
  soma_quadrados_diferencas = 0
  for valor in dados:
    soma_quadrados_diferencas += (valor - media_valores)**2
  return st.sqrt(soma_quadrados_diferencas / len(dados))


for empresa, serie_salarios in dados.items():
  print(f"**{empresa}**")
  print(f"Média: R$ {mediaSalario(serie_salarios):,.2f}")
  print(f"Moda: R$ {modaSalario(serie_salarios)}")
  print(f"Mediana: R$ {medianaSalario(serie_salarios):,.2f}")
  print(f"Desvio Padrão: R$ {desvio(serie_salarios):,.2f}")
  print()


melhores_empresas = []

for empresa, serie_salarios in dados.items():
  if (medianaSalario(serie_salarios) >= 4000) and (desvio(serie_salarios) < 3000):
    melhores_empresas.append(empresa)


print("A melhor empresa que eu escolhi devido a Média:")
for empresa in melhores_empresas:
  print(f"- {empresa}")

