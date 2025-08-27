# Arquivo de configuração de dataclasses
# A ideia desse arquivo é configurar as classes de armazenamento utilizadas na captura de informações

from dataclasses import dataclass

@dataclass
class Row:
    invoice_number: str
    invoice_date: str
    invoice_url: str
