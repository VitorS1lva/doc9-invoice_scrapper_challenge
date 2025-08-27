# Libs
import sys
import time
from typing import List

# Funcs
from general_functions.logger_config import setup_logger
from general_functions.clear_output_dir import clean_output_dir
from general_functions.csv_parse import save_rows_csv
from process.get_rows import get_rows
from general_functions.types import Row

def main():
    # Início do cronômetro
    start_time = time.perf_counter()

    # Configura logger customizado
    logger = setup_logger()

    # Limpando pasta de output, evita acúmulo de arquivos
    clean_output_dir()
    
    try:
        # Chamando função que navegapela tabela da aplicação  
        logger.info("Iniciando scraping da tabela")
        rows: List[Row] = get_rows(logger)
    finally:
        # Escrevendo CSV
        logger.info(f"Parseando csv com dados extraídos")
        save_rows_csv(rows)
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
