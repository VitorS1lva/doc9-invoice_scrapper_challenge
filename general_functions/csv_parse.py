import csv
import logging
from datetime import datetime
from dataclasses import asdict, is_dataclass
from common_vars import output_dir
from typing import List, Union, Dict, Any

def save_rows_csv(rows: List[Union[Any, Dict[str, Any]]]) -> str:
    """
    Salva os dados extraídos do site em um arquivo CSV.
    """
    if not rows:
        logging.warning("Nenhum dado para salvar no CSV")
        return ""

    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file_path = output_dir / f"doc9_results_{timestamp}.csv"
        
        # Processa a primeira linha para determinar headers
        first_row = rows[0]
        if is_dataclass(first_row):
            first_row_dict = asdict(first_row)
            headers = list(first_row_dict.keys())
        elif isinstance(first_row, dict):
            headers = list(first_row.keys())
        else:
            raise TypeError(f"Tipo inválido em rows: {type(first_row)}. Esperado dataclass ou dict.")

        # Escreve CSV de forma otimizada
        with open(output_file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            
            # Processa e escreve as linhas em lote
            for row in rows:
                if is_dataclass(row):
                    writer.writerow(asdict(row))
                else:
                    writer.writerow(row)

        logging.info(f"Arquivo CSV criado com sucesso: {output_file_path}")
        return str(output_file_path)

    except Exception as e:
        logging.error(f"Erro ao salvar CSV: {str(e)}")
        raise