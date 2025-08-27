# Invoice Scrapper Doc9 — Automation Challenge

Este repositório contém a solução para o desafio de automação do processo seletivo da Doc9. O objetivo do projeto é automatizar a extração de informações de faturas (invoices) a partir de uma aplicação web, realizando o download dos arquivos PDF e salvando os dados relevantes em arquivos CSV, com registro detalhado de logs de execução.

## Propósito Geral

Automatizar o processo de coleta de dados de faturas em uma plataforma web, incluindo:
- Navegação automatizada via Selenium WebDriver.
- Extração de dados tabulares (número da fatura, data, link para download).
- Download automático dos arquivos PDF das faturas.
- Filtragem de dados conforme a data de vencimento.
- Geração de relatórios em CSV.

## Principais Pontos do Projeto

## Como Executar

# 1) instalar dependências
pip install -r requirements.txt

# 2) executar
python main.py

## Estrutura do Projeto

- `main.py` — Orquestra o fluxo principal da automação.
- `general_functions/` — Configuração, logger e tipos de dados.
- `process/` — Funções de scraping e manipulação de dados.
- `utils/` — Utilitários para Selenium, manipulação de arquivos e datas.
- `output/` — Resultados gerados pela automação.
- `logs/` — Arquivos de log de execução.

---