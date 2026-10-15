# Triagem da gravidade de acidentes em rodovias federais com Multilayer Perceptrons

Trabalho prático final da disciplina de Deep Learning (Especialização em Inteligência Artificial Aplicada, IFG Câmpus Goiânia), frente 3.1 Multilayer Perceptrons.
Autor: Igor Coutinho Ferreira Nobre. Professor: Prof. Dr. Sérgio Canuto.

## Resumo

Quando alguém liga para a PRF para relatar um acidente, a central precisa decidir o que enviar com pouca informação. O trabalho treina uma MLP em PyTorch para estimar a gravidade do acidente (`Sem Vítimas`, `Com Vítimas Feridas` ou `Com Vítimas Fatais`) a partir do que o solicitante consegue informar: tipo de acidente, quantidade de veículos e pessoas, local, horário e condições da via. É um problema de classificação multiclasse sobre 2,2 milhões de acidentes registrados pela PRF entre 2007 e 2026.

As 12 entradas são categóricas e passam por one-hot (194 colunas). O ano e a causa detalhada ficam de fora de propósito, porque refletem a mudança no procedimento de registro da PRF ao longo dos anos, e não a gravidade. A busca de hiperparâmetros usou busca bayesiana (Optuna, TPE) com 25 tentativas; as três melhores arquiteturas foram treinadas com toda a base de treino e avaliadas uma única vez no teste.

Resultado: o modelo final, com uma camada oculta de 172 neurônios (34 mil parâmetros), obteve 70,3% de acurácia e Macro F1 de 0,607 no teste, contra 68,5% e 0,588 da regressão logística com as mesmas entradas. A largura da rede importou mais que a profundidade, o dropout foi a regularização mais eficaz e o relato do solicitante respondeu pela maior parte do desempenho.

## Onde está cada coisa

| Item | Caminho |
| --- | --- |
| Relatório técnico (PDF) | [`relatorio.pdf`](relatorio.pdf) |
| Notebook executado (EDA, pré-processamento, Optuna, avaliação) | [`app/trabalho_final_mlp_prf_simples.ipynb`](app/trabalho_final_mlp_prf_simples.ipynb) |
| Dataset | `app/datasets/datatran2007.csv` a `datatran2026.csv`, um arquivo por ano (não versionados, 475 MB; ver abaixo) |
| Registro da busca de hiperparâmetros | [`app/artifacts_simples/optuna_trials.csv`](app/artifacts_simples/optuna_trials.csv) e [`config_final.json`](app/artifacts_simples/config_final.json) |
| Tabelas de resultado (teste, baselines, ablações) | [`app/artifacts_simples/`](app/artifacts_simples/) (arquivos `.csv`) |
| Figuras | [`app/artifacts_simples/figuras/`](app/artifacts_simples/figuras/) |
| Pesos dos três modelos finais e encoder | `app/artifacts_simples/mlp_M1.pt`, `mlp_M2.pt`, `mlp_M3.pt`, `onehot_encoder.pkl` |
| Instruções de ambiente e execução | [`app/README.md`](app/README.md) |

## Dataset

Fonte: "Acidentes nas Rodovias Federais (agrupados por ocorrência)", Polícia Rodoviária Federal, Portal Brasileiro de Dados Abertos:
https://dados.gov.br/dados/conjuntos-dados/sinistros-de-transito-agrupados-por-ocorrencia

São 20 arquivos CSV (`datatran2007.csv` a `datatran2026.csv`, separador `;`, codificação latin-1), com uma linha por acidente. Eles não estão no repositório por causa do tamanho. Para reproduzir, baixe os arquivos anuais no link acima e coloque-os em `app/datasets/`.

## Como rodar

```bash
cd app
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./start_jupyter.sh
```

Abra `trabalho_final_mlp_prf_simples.ipynb` e execute as células em ordem. A execução completa leva cerca de 35 a 40 minutos em CPU e usa cerca de 4 GB de RAM; as sementes são fixas, então as métricas se repetem. Detalhes em [`app/README.md`](app/README.md).
