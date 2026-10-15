# Triagem Preditiva de Acidentes da PRF com MLP

Trabalho prático final da disciplina de Deep Learning (Pós IFG), frente 3.1 Multilayer Perceptrons.
Autor: Igor Coutinho Ferreira Nobre.

Classificação multiclasse da gravidade do acidente (`classificacao_acidente`: sem vítimas, com feridos, com mortos)
com uma MLP em PyTorch e busca de hiperparâmetros via Optuna, usando os 20 anos de dados da PRF (2007 a 2026, 2,24 milhões de acidentes).
As 12 entradas são categóricas e passam por one-hot (194 colunas). O ano e a causa detalhada ficam de fora de propósito,
porque refletem a mudança no procedimento de registro da PRF ao longo dos anos, e não a gravidade.

Resultado no teste: 70,3% de acurácia e Macro F1 0,607 com uma MLP de 1 camada oculta (194 → 172 → 3, 34 mil parâmetros).

Fonte dos dados: "Acidentes nas Rodovias Federais (agrupados por ocorrência)", PRF, Portal Brasileiro de Dados Abertos:
https://dados.gov.br/dados/conjuntos-dados/acidentes-rodovias-federais

## Estrutura

```
trabalho_final_mlp_prf.ipynb   notebook executado: EDA, pré-processamento, Optuna, avaliação
artifacts/                     encoder, pesos dos 3 modelos finais, trials do Optuna, tabelas de resultado e figuras
datasets/                              arquivos datatran2007.csv a datatran2026.csv da PRF (não versionados)
requirements.txt                       dependências fixadas
start_jupyter.sh                       sobe o Jupyter usando o .venv desta pasta
```

Os CSVs da PRF não estão no repositório por causa do tamanho (475 MB). Para reproduzir, baixe os arquivos anuais
no link acima e coloque-os em `datasets/`.

## Como rodar

```bash
cd app
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name trabalho-dl --display-name "Python 3 (.venv trabalho DL)"
./start_jupyter.sh                   # Jupyter nesta pasta, porta 8888
```

Para executar tudo sem abrir a interface (cerca de 35 a 40 minutos em CPU, ~4 GB de RAM):

```bash
python -m nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=7200 trabalho_final_mlp_prf.ipynb
```

As sementes são fixas, então as métricas se repetem entre execuções.
