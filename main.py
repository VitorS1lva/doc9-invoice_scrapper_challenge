# Libs
import sys
import time
from typing import List

# Funcs
from general_functions.logger_config import setup_logger

def main():
    # Início do cronômetro
    start_time = time.perf_counter()

    # Configura logger customizado
    logger = setup_logger()
    
    try:
        # Chamando função que navegapela tabela da aplicação  
        logger.info("Iniciando scraping da tabela")
    finally:
        # Fim do cronômetro
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        logger.info(f"Tempo de execução: {elapsed:.2f} segundos")
    
    logger.info(f"Processo finalizado com sucesso")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Criando fallback pra caso dar erro fatal antes da inicialização do logger
        print(f"Erro fatal: {e}", file=sys.stderr)
        sys.exit(1)
