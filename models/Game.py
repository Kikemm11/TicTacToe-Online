"""
Authors:
- Iván Maldonado (Kikemaldonado11@gmail.com)
- Maria José Vera (nandadevi97816@gmail.com)
- Sergio Fernández (sergiofnzg@gmail.com)

Developed at: October 2024
"""

from models.Table import Table

class Game():
    
    def __init__(self):
        self.tables = []
        self.table_id = 1
          
    def create_table(self):
        table = Table(self.table_id)
        self.tables.append(table)
        self.table_id += 1