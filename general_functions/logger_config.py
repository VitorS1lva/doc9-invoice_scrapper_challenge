import logging
from datetime import datetime
from pathlib import Path
from common_vars import log_dir, process_name

# Variável global para controlar se algum handler já foi adicionado
_logger_configured = False

def setup_logger() -> logging.Logger:
    """
    Configura um logger customizado que gera logs em arquivos .txt
    Um novo arquivo é criado a cada execução.
    
    Formato das mensagens:
    DD/MM/YYYY_HH:MM:SS - NomeDoProcesso - LEVEL - Mensagem
    """
    global _logger_configured
    
    logger = logging.getLogger(process_name)
    
    if _logger_configured:
        return logger
    
    # Formatando o nome que vai no arquivo
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = log_dir / f"Execução_{process_name}_{timestamp}.txt"

    # Formatando a mensagem que o logger exibe
    log_format = logging.Formatter(
        fmt=f"%(asctime)s - {process_name} - %(levelname)s - %(message)s",
        datefmt="%d/%m/%Y_%H:%M:%S"
    )

    # Configura o nível do logger
    logger.setLevel(logging.INFO)
    
    # Trata algum handler que jáe xista
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Handlers do log
    # Para arquivo
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    # Para o console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # Desabilita propagação para o logger root para evitar duplicação
    logger.propagate = False
    
    # Alterna o boleano chave criado no topo do código
    _logger_configured = True
    
    logger.info(f"Logger inicializado — arquivo: {log_file.resolve()}")
    return logger