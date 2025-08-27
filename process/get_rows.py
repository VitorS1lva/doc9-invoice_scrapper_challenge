import asyncio
import aiohttp
import requests
from typing import List
from datetime import datetime
from general_functions.types import Row
from common_vars import base_url, output_dir

async def download_pdf(session: aiohttp.ClientSession, url: str, path):
    """
    Função para baixar o PDF
    """
    async with session.get(url) as response:
        content = await response.read()
        with open(path, "wb") as f:
            f.write(content)


async def download_all_pdfs(pdf_tasks):
    """
    Função para baixar todos os PDFs em paralelo, usa a função de download_pdf
    """
    async with aiohttp.ClientSession() as session:
        tasks = [download_pdf(session, url, path) for url, path in pdf_tasks]
        await asyncio.gather(*tasks)


def get_rows(logger) -> List[Row]:
    """
    Coleta uma resposta da API juntando o url+/seed, esses valores foram encontrados nas ferramentas de inspeção do navegador
    Inspecionar > Network
    """
    logger.info("Fazendo requisição para o endpoint")
    
    # INicializando ariáveis da função
    rows = []
    pdf_tasks = []
    today = datetime.today().date()

    # Header da requisição
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest'
    }

    # PIngando requisição API
    response = requests.post(f"{base_url}/seed", headers=headers, timeout=10)
    data = response.json()

    # Processa dados da resposta
    for item in data['data']:
        invoice_number = item['id']
        invoice_date_str = datetime.strptime(item['duedate'], "%d-%m-%Y").date() # Já captura o valor formatando para a data atual
        invoice_url = f"{base_url}{item['invoice']}"

        # Atende a regra do desafio, só baixa faturas vencidas ou com data de hoje
        if invoice_date_str <= today:
            rows.append(Row(
                invoice_number=invoice_number,
                invoice_date=invoice_date_str,
                invoice_url=invoice_url
            ))

            #Download dos PDFs
            pdf_name = item['invoice'].split('/')[-1]
            pdf_path = output_dir / pdf_name
            pdf_tasks.append((invoice_url, pdf_path))
        else:
            continue

    # Faz downloads em paralelo para otimizar mais tempo
    if pdf_tasks:
        asyncio.run(download_all_pdfs(pdf_tasks))

    logger.info(f"Concluído: {len(rows)} faturas vencidas processadas")
    return rows