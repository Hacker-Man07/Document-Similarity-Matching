from typing import List, Dict

class InvoiceDatabase:
    def __init__(self):
        self.invoices = []

    def add_invoice(self, invoice: Dict[str, str]):
        self.invoices.append(invoice)

    def get_all_invoices(self) -> List[Dict[str, str]]:
        return self.invoices
