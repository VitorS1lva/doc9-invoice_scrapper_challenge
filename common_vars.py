# Este arquivo armazena variáveis globais comuns a serem utilizadas ao longo do processo de automação
from pathlib import Path

# Caminho absoluto da raiz do projeto
project_root = Path(__file__).resolve().parent

# Definindo pasta padrão de saída "output" e fazendo uma verificação de existência
output_dir = project_root / "output"
output_dir.mkdir(parents=True, exist_ok=True)

# Nome do processo
process_name = "[Doc9 - Invoice Scraper]"

# Diretório de logs
log_dir = project_root / "logs"
log_dir.mkdir(parents=True, exist_ok=True)

# uRL base a ser acessada para scrapping
base_url = "https://rpachallengeocr.azurewebsites.net"