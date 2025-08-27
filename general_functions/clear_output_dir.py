import logging
import shutil
from common_vars import output_dir

# Este arquivo armazena funcões uteis a serem utilizadas ao longo do processo de automação

# Função que limpa a pasta de output antes de cada execução
def clean_output_dir():
    """
    Limpa o conteúdo da pasta output na raiz do projeto.
    Não remove a pasta em si, apenas os arquivos e subpastas dentro.
    """
    try:
        if output_dir.exists() and output_dir.is_dir():
            for item in output_dir.iterdir():
                try:
                    if item.is_file() or item.is_symlink():
                        item.unlink()  # remove arquivo
                    elif item.is_dir():
                        shutil.rmtree(item)  # remove subpasta
                except Exception as inner_e:
                    logging.warning(f"Não foi possível excluir {item}: {inner_e}")

            logging.info(f"Conteúdo da pasta output limpo: {output_dir}")

    except Exception as e:
        logging.error(f"Erro ao limpar a pasta output: {str(e)}")
        raise
