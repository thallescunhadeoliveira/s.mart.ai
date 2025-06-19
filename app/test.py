import ast

date_compra = "[2019, 10, 19, 10, 20, 9]"  # tipo: str
lista = ast.literal_eval(date_compra)     # funciona
print(type(lista))        # [2019, 10, 19, 10, 20, 9]